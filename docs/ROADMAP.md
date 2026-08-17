# Cortex V6 Roadmap

This file is a human-readable index of tracked work. GitHub issues remain the authoritative work items.

## P0 — bootstrap and first proof

- #1 — bootstrap governance, durable docs, and traceability gate. **Bootstrap complete; branch enforcement remains #8.**
- #2 — establish ordinary SWE foundation and CI before kernel work.
- #3 — prove one real walking skeleton end to end.
- #4 — recover V4 stable task-state and context-preservation invariants.
- #8 — require the docs gate through GitHub branch protection/rulesets.

## P1 — migration and negative controls

- #5 — qualify useful V5 donor components individually.
- #6 — replace SSC v1 runtime seams and prove FOSSIL-backed context.
- #7 — encode SCC v2 failures as V6 adversarial/system tests.

## Dependency shape

```text
#1 governance
 |
 +--> #8 GitHub enforcement
 |
 v
#2 SWE foundation
 |
 v
#3 walking skeleton
 |\
 | +--> #5 V5 donor qualification
 | +--> #7 SCC v2 failure tests
 v
#4 V4 state/context recovery
 |
 v
#6 SSC v1 retirement + FOSSIL context
```

## Backlog admission rule

Do not add a roadmap node because a capability sounds useful. A new issue that proposes architecture should identify:

1. the observed problem;
2. the simplest/conventional baseline;
3. evidence or experiment showing the gap;
4. alternatives/mature dependencies considered;
5. new failure modes introduced;
6. an acceptance test that can falsify the proposal.

Research may exist without a committed architecture boundary.
