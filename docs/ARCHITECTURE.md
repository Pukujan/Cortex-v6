# Cortex V6 Architecture — Recovery Baseline

**Status:** minimal recovery baseline. This document intentionally does not describe future subsystems that have not earned a boundary.

## Current system target

```text
Human request
      |
      v
Stable Requirement/Task State
      |
      v
Bounded Context Controller
      |
      v
One Work Unit
      |
      v
Controlled Effect
      |
      v
Independent Verification
      |
      v
Evidence-bound Result
```

The first acceptance path is deliberately smaller than V4, V5, or SCC v2. Its purpose is to establish the composition rules on which later capabilities can be tested.

## Core distinctions

### Semantic task state is not transcript

The system must retain explicit goals/constraints/accepted decisions/unresolved questions/completion criteria independently of conversational history.

### Working context is not durable knowledge

Working context is temporary, bounded material selected for a task. Protected semantic task state cannot be silently compacted away.

Durable evidence/knowledge will be supplied by FOSSIL through a narrow provider when #6 begins. FOSSIL does not own active task execution state.

### Execution result is not verification

The executor produces an effect/result. A separate verification path decides whether the declared acceptance condition is satisfied. Worker/model self-report is not completion evidence.

### Component correctness is not composition correctness

A component is not considered protective merely because it exists or its unit tests pass. Critical acceptance tests must traverse the same composition path used by real work.

## First interfaces — provisional

Only introduce interfaces required by the walking skeleton. Initial candidates are:

- `RequirementState` — stable authoritative task semantics;
- `ContextProvider` / bounded context controller — evidence/context seam;
- `WorkUnit` — one bounded executable unit;
- `ExecutionPort` — controlled effect boundary;
- `VerificationPort` — independent mechanical verdict.

These names are provisional until implementation pressure confirms them. Do not build a general plugin/capability framework around them yet.

## Initial invariants

1. A task cannot execute without stable task/requirement state.
2. Protected semantic state cannot disappear due to context compaction.
3. An effect cannot write outside its declared authority.
4. Verification cannot be satisfied by executor/model assertion alone.
5. Completion evidence binds to the exact authoritative input/work-unit version.
6. Stale/mismatched results cannot complete a newer task state.
7. A system acceptance test traverses the production composition path.

## Explicitly unresolved

The following are research topics, not current architecture:

- whether requirements/risk/planning/decomposition deserve separate product boundaries;
- plugin/module architecture for methodologies;
- formal-method selection;
- risk tiering;
- PDD/TDD/BDD/SDD strategy composition;
- arbitration and multi-model topology;
- generalized capability registries;
- long-term learning/calibration systems.

Each needs its own tracked falsifiable case before becoming architecture.

## Architecture change rule

If a PR changes a durable boundary, authoritative state owner/writer, lifecycle transition, or trust assumption, it must update this document or another durable design document and explain the change in its tracking issue.
