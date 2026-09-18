# The verifier gate

These are the checks the verifier seat runs against a builder's work
product before it reaches the human tap. Adapt the lists to your domain;
keep the discipline.

## Universal checks (every work product)

- [ ] Re-read the actual output, not the builder's summary of it.
- [ ] Check it against the work order's done criteria, one by one.
- [ ] Verdict format: **ready / not-ready**, what changed, how far the
      work was from shippable. Heavy edits get flagged back on the
      builder — the operator should see the pattern, not just the fix.
- [ ] No secrets, credentials, tokens, or personal data in the output.
- [ ] No invented facts: names, numbers, quotes, titles, statuses are
      either sourced or absent.

## Publishing checks (anything that goes public)

- [ ] Featured image set *before* the publish tap — never after.
- [ ] `og:image` (and social preview) verified on the live URL.
- [ ] Headline, byline, date, category correct on the live page.
- [ ] **Real visual QA: desktop AND mobile, in a real browser.**
      API/source/HTTP checks are not verification. Rendered output is
      the only thing that counts — automated checks once passed an
      article with invisible white-on-cream text.
- [ ] Sensitive-token scrub: exact matches block, fuzzy matches go to
      human review. Redact to generic nouns ("a client site," never
      names); specific live vulnerabilities are never published.

## Send checks (email, messages, posts)

- [ ] Recipient, subject, and exact body confirmed with the operator
      before sending. The operator's tap names the send.
- [ ] Send-once: keyed on the work-order key. Check the sent record
      before any retry — never blind-retry a send.
- [ ] Identity correct: the message discloses which seat sent it and
      never impersonates the operator.

## Batch-work checks (scripts, bulk writes, migrations)

- [ ] Writes paced (8–10s apart for API writes is a sane default).
- [ ] Every response re-read; never blind-retry a truncated or
      ambiguous write.
- [ ] Positive evidence required for success: a marker string, a file
      that exists, a real response. Absence of a failure signal is not
      a pass.
- [ ] Check system load before starting bulk work; schedule heavy runs
      for idle windows.

## When the verifier fails work

Not-ready means: what failed, which checklist item, and the smallest
fix that would pass. The verifier fixes trivia itself, sends substance
back to the builder, and tells the operator which one it was. A builder
that keeps failing the same check is a builder problem — say so.
