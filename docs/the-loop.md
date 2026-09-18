# The loop

## The pattern

Most agent setups are one prompt, one session: you ask, it answers, you
hope. The governed loop turns that into a pipeline with named seats and
a gate that work has to pass.

**Seats:**

- **Operator (human).** Defines intent and guardrails, holds the final
  tap. Does not do fiddly verification — that's the verifier's job.
- **Builder (agent).** Does the work: writes code, drafts articles,
  runs uploads, processes batches. Optimized for throughput.
- **Verifier (agent).** A *separate* seat from the builder. Re-reads the
  work product, runs the written checklists, looks at rendered output
  with real eyes (browser, screenshots), and returns a verdict:
  ready / not-ready, what changed, and how far the work was from
  shippable. Heavy edits get flagged back on the builder.

**Flow:**

1. Operator issues a **work order** (structured, idempotency-keyed).
2. Builder executes, returns the work product.
3. Verifier checks it against the written gate checklists.
4. Operator gets a clean verdict and holds one tap: ship, fix, or park.

The builder never grades its own homework. The verifier never ships.
The operator never verifies fiddly details — that's what the verifier
is for.

## Where this came from

Inspired by Atlassian's governed agent loops for the AI-native SDLC
(Jira): well-defined tickets get picked up by coding agents, run
through automated testing, and land as ready-to-review pull requests
only after every test passes — with AI review checking each PR against
organizational standards and a human holding the merge button.

Their finding, from DX's analysis of hundreds of organizations: teams
with dense, current shared context shipped ~64% more per developer.
Context is the multiplier; the agent is the commodity.

## Where it differs — and why

| Atlassian's loop | This loop |
|---|---|
| Built for engineering orgs on Jira | Built for a solo operator with agent seats |
| Ticket = Jira issue | Ticket = structured work order (email, chat, file) |
| Gate = automated tests + standards-as-code | Gate = verifier agent + written checklists |
| AI review checks code against standards | Verifier checks work against checklists *with eyes* |
| Context = Teamwork Graph | Context = operator's knowledge base + memory |
| Human holds the merge button | Human holds the tap on ship/send/publish/spend |

The core difference is the gate. A deterministic gate (tests) never
forgets and runs the same way every time — but it only catches what
someone thought to test for. A judgment gate (verifier agent with
written checklists) catches the things nobody wrote a test for: the
article that rendered white text on a cream background and passed every
automated check, the tone that's technically correct and completely
wrong, the factual claim that's plausible and false.

The failure mode of a judgment gate is memory: it lives in an agent's
context, and contexts compact. That's why every check is written down
in `the-verifier-gate.md`. A check that only lives in a session dies
with the session. Written checklists are how a judgment gate becomes
durable.

Run both kinds of gate when you can. Never ship with neither.
