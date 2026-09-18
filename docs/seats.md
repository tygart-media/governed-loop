# Seats

## The three seats

**Builder.** Does the work. Optimized for throughput: code, drafts,
uploads, bulk processing, research. The builder's permissions come from
the work order's guardrails — it may not send, publish, spend, touch
credentials, or delete unless the work order explicitly allows it
(and the human tap still governs the one-way doors).

**Verifier.** A separate agent seat from the builder. It never builds;
it checks. It runs `the-verifier-gate.md` against the work product and
returns ready / not-ready, what changed, and how far the work was from
shippable. It fixes trivia, bounces substance back to the builder, and
flags repeat failure patterns to the operator.

**Operator (human).** Defines intent and guardrails, holds the final
tap on ship / send / publish / spend. The operator does not do fiddly
verification — that's the verifier's job. The operator's calibration
rule: a live utterance outranks a stored rule on two-way doors
(momentum wins); on one-way doors the stored rule holds and the
operator overrides explicitly.

## Why separate the verifier

The builder is optimized to finish. Finishing and verifying are
opposed instincts — the seat that did the work will always grade its
own homework generously. A separate verifier with no authorship stake
reads the work cold, which is the closest an agent gets to fresh eyes.

## Model routing (optional, advanced)

When the choice of model matters, log **model × job-shape × outcome**
for runs you actually observed — no backfilled fiction, no benchmark
guesses. Over time the log becomes a picker: match the model's shape
to the job instead of defaulting to one model for everything. Static
one-shot jobs stay on whatever's cheapest; jobs where the answer picks
the next step get the driving seat.

## Adding seats

Name them, give each a watched subject line or channel, write down what
each may touch, and add the verifier's checklists for the new domain.
A seat with no written permissions has no permissions.
