# Governed Loop

A human-governed operating pattern for running AI agent seats without
letting them wreck things. Work goes out as structured work orders, a
builder seat does the work, a verifier seat checks it against written
checklists, and a human holds the final tap. Nothing ships without
passing the gate.

Inspired by Atlassian's governed agent loops (ticket → agent → tests →
AI review → human merge). The difference: this loop was built for a
solo operator, not an engineering org — and the gate is a verifier
*agent* plus written checklists, not a test suite. Judgment catches
what tests can't.

```
operator defines intent + guardrails
        │
        ▼
   ┌──────────┐
   │  BUILDER │  does the work (code, drafts, uploads)
   └────┬─────┘
        │ work product
        ▼
   ┌──────────┐
   │ VERIFIER │  checks against written checklists,
   │  (agent) │  re-reads, looks with real eyes
   └────┬─────┘
        │ pass / fail + what changed
        ▼
   ┌──────────┐
   │  HUMAN   │  one tap: ship / fix / park
   │   TAP    │
   └──────────┘
```

## The rules that make it governed

1. **Work orders, not prompts.** Every delegation is a structured work
   order with a deterministic idempotency key. Same key = same work;
   never send twice. See `docs/work-orders.md`.
2. **The verifier is a separate seat.** The builder never grades its own
   homework. The verifier re-reads everything, checks the checklists,
   and reports ready / not-ready plus how far the work was from
   shippable.
3. **Written checklists beat memory.** Every check the verifier runs is
   written down in `docs/the-verifier-gate.md`. A check that only lives
   in an agent's context dies with the session.
4. **The human tap is the gate.** Nothing publishes, sends, or spends
   without an explicit human approval. A thumbs-up means "seen," not
   "yes."
5. **Idempotency lives in the tooling.** Proactive sends go through
   send-once keyed on the work-order key. An approval timeout is never
   proof a send failed — check the sent record before retrying.

## Quickstart

1. Read `docs/the-loop.md` for the pattern.
2. Copy `scripts/work_order.py` and issue your first work order.
3. Run the verifier checklists in `docs/the-verifier-gate.md` against
   whatever comes back.
4. Hold the tap. Ship, fix, or park.

## Where this differs from Atlassian's loop

See `docs/the-loop.md` — the short version: their gate is
deterministic (tests, standards-as-code, AI review against standards).
Ours is judgmental (a verifier agent with eyes, written checklists, a
human with taste). Deterministic gates never forget; judgment gates
catch the white-text-on-cream-background bug that passed every
automated check. Run both when you can; never ship with neither.

## Take it, make it better

Standard invitation: take this, make it better — if you build something
better, come back. We'll be customer #1 and we'll pay you for it.

## License

MIT. See `LICENSE`.
