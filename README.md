# Cortex V6

Cortex V6 is a clean recovery experiment for the Cortex lineage. It is **not** a feature expansion of V5 and it is not a rewrite of SCC v2.

The first objective is to prove one small, real, mechanically governed path before adding new architecture:

```text
human request
  -> stable requirement/task state
  -> bounded context
  -> one work unit
  -> controlled effect
  -> independent verification
  -> result
```

## Lineage roles

- **SSC v1** — legacy methodology/corpus source to be retired as a live dependency.
- **SCC v2** — experiment and failure corpus; source of adversarial tests, not a runtime dependency.
- **Cortex V4** — behavioral reference for stable task state, bounded context, action gating, and replay semantics.
- **Cortex V5** — donor implementation; components must be qualified individually before reuse.
- **FOSSIL** — durable knowledge/evidence owner; it does not own Cortex operational workflow state.

## Development rule

V6 grows one proven path at a time. New mechanisms require a tracked issue, an explicit problem, consideration of mature/simple alternatives, and a measurable acceptance condition.

The repository was empty when bootstrap issue #1 was opened. Issue #1 is the one-time exception authorizing the initial governance/docs commits directly to `main`. After bootstrap, substantive work is expected to use linked issues, pull requests, and the repository gates.

See:

- `docs/PROJECT.md` — scope and recovery strategy
- `docs/ARCHITECTURE.md` — minimal current architecture and invariants
- `docs/GOVERNANCE.md` — issue/PR/docs policy
- `docs/ROADMAP.md` — tracked issue order

## Current milestone

No kernel implementation yet. The current milestone is repository governance and the ordinary SWE foundation tracked by #1 and #2.
