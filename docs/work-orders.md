# Work orders

A work order is a structured delegation with a deterministic idempotency
key. It replaces the vague prompt with something a seat can execute and
a verifier can check.

## Format

```
WORK ORDER <YYYYMMDD>-<slug>          # the idempotency key
To: <builder seat>
Subject: <seat-name> <key> <short intent>   # seat watches its subject line

INTENT
  What done looks like, in one paragraph.

GUARDRAILS
  What the builder must not touch: no sends, no publish, no spend,
  no credentials, no deletions — list the ones that apply.

INPUTS
  Links, files, threads, prior work the builder should read first.

DONE CRITERIA
  Checkable conditions. "Article live at URL, featured image set,
  og:image verified, desktop + mobile visually checked."

REPORT BACK
  What the builder returns: what changed, files touched, what needs
  the verifier's eyes, anything uncertain.
```

## Rules

1. **Deterministic key.** `<YYYYMMDD>-<slug>` derived from the work, not
   random. Same work = same key. The key is the dedup identity for
   everything downstream.
2. **Send-once.** A work order is sent exactly once per key. If a send
   seems to have failed, check the sent record before retrying — an
   approval timeout is never proof the send failed.
3. **Subject-line discipline.** Seats watch subjects, not bodies. Put
   the seat name and the key in the subject so the right seat picks it
   up and duplicates are visible at a glance.
4. **Guardrails are explicit.** "Don't publish" is not implied by
   context — it's written in the work order. The builder's permissions
   come from the work order, not from vibes.
5. **Done criteria are checkable.** If the verifier can't check it, it
   isn't a done criterion. "Looks good" is not checkable. "Featured
   image set and og:image verified" is.

## Generating one

`scripts/work_order.py` renders the template with a deterministic key:

```
python3 scripts/work_order.py --seat builder --slug "q3-pricing-page" \
  --intent "Rebuild the pricing page from the approved copy deck." \
  --out work-orders/
```
