# Cortex V6 Project Charter

## Purpose

Cortex V6 exists to recover the strongest proven behaviors of earlier Cortex work while removing accidental coupling, context corruption, and architecture that has not earned its complexity.

V6 is a **subtractive recovery program**. The default decision for a new mechanism is **do not add it** until the current walking skeleton demonstrates a concrete need.

## Immediate success criterion

The first executable milestone is exactly one real path:

```text
human request
  -> stable RequirementState
  -> bounded/protected working context
  -> one WorkUnit
  -> controlled filesystem effect
  -> independent exact-output verification
  -> completion evidence
```

The path must be the same path exercised by the system test. No fake production composition is allowed for acceptance.

## Non-negotiable invariants

1. The human owns scope and completion.
2. Conversation/transcript is not authoritative task truth.
3. Stable task/requirement semantics are represented separately from working context.
4. Consequential effects require explicit authority.
5. Working context is bounded and protected semantic state cannot be silently dropped.
6. Model/worker output is not verification evidence by itself.
7. Completion requires evidence bound to the exact task/work-unit version.
8. Stale attempts/results cannot advance newer authoritative state.
9. Durable knowledge belongs to FOSSIL; operational task state belongs to Cortex.
10. Component/unit correctness never substitutes for composition correctness.

## Explicit non-goals until earned by evidence

V6 does not currently commit to separate products or frameworks for:

- risk tiering;
- phase planning;
- decomposition/granularity;
- methodology classification;
- PDD/TDD/BDD/SDD strategy selection;
- TLA+ or other formal methods;
- arbitration;
- capability registries or package managers;
- autonomous learning;
- multi-agent fanout;
- a universal plugin architecture.

These remain research hypotheses until an issue demonstrates a problem, a simpler baseline, measurable benefit, and an acceptance test.

## Lineage use

### SSC v1
Legacy reference/provider only. V6 must ultimately run with SSC v1 unavailable.

### SCC v2
Negative-control source. Its failure reports become V6 adversarial/system tests where applicable.

### Cortex V4
Behavioral reference for stable task state, bounded context, protected spans, action gates, replay/fencing, and methodology behaviors that are proven useful.

### Cortex V5
Donor code. Reuse is per-component and evidence-based; V5 runtime composition is not inherited automatically.

### FOSSIL
Durable evidence/knowledge service. V6 consumes it through narrow seams when #6 begins; V6 does not move operational task state into FOSSIL.

## Build order

1. #1 governance/docs gate.
2. #2 ordinary SWE foundation.
3. #3 one real walking skeleton.
4. #4 recover V4 state/context invariants.
5. #5 qualify useful V5 donor pieces.
6. #6 remove SSC v1 live dependency / attach FOSSIL-backed context.
7. #7 encode SCC v2 failures as adversarial composition tests.

Expansion beyond this list requires its own tracked evidence.
