# Cortex V6 Architecture — Recovery Baseline

**Status:** minimal kernel recovery baseline plus the locked provider-ownership direction from #9. Detailed mechanisms remain falsifiable at their tracked qualification gates. See `docs/V6_LOCKED_PLAN.md` for the full handoff.

## Current system target

The first acceptance path remains deliberately smaller than the eventual provider-integrated system:

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

This path must be proven before runtime frameworks, dynamic assurance routing, FOSSIL composition, or multi-agent topology are allowed to become production dependencies.

## Locked ownership direction

### Project owns WHAT must be true

The project is authoritative for current requirements, constraints, source, tests, config, ADRs, acceptance conditions, SLO/security/performance requirements, project benchmarks, and explicit human decisions.

V6 may bind an exact snapshot/version for a work generation, but it does not silently redefine project acceptance meaning.

### Cortex V6 owns CONTROL

V6 owns only the semantics that must remain stable across runtimes/providers:

- authoritative task/work lifecycle state;
- exact requirement/work-unit/generation identity;
- scope/authority grants;
- task/risk/topology routing;
- model seating semantics;
- assurance obligations;
- evidence admission and exact-version binding;
- retry / blocked / verifying / complete transitions.

### FOSSIL owns KNOWLEDGE

FOSSIL owns durable evidence, provenance, lineage, source-quality metadata, historical/reusable knowledge, disagreement/supersession, and knowledge-graph/retrieval projections.

FOSSIL does not own active Cortex task state. Live project sources remain authoritative for current project facts when they differ from stale durable memory.

### External runtime owns EXECUTION INFRASTRUCTURE

The runtime substrate may own sessions, sandbox/isolation, tool transport, runtime credentials/identity, telemetry/traces, and provider-specific policy enforcement.

The first runtime candidate is Microsoft Agent Framework (#11). AWS AgentCore is a later portability challenger (#12).

A vendor session/thread/ARN/managed-identity object is never itself an authoritative Cortex task.

### LiteLLM owns MODEL TRANSPORT

LiteLLM remains the model/provider transport boundary. V6 may own semantic model seating/ranking/retry policy, but provider protocol details stay outside authoritative task state (#19).

### Assurance providers own METHOD EXECUTION

Pytest, Hypothesis/PBT, mutation frameworks, BDD tools, TLA+/TLC, theorem provers/SMT, security tools, benchmarks, fault/chaos tooling, critics, and holdouts remain external assurance providers.

They produce evidence. They cannot directly mark a V6 task complete.

### GitHub/CI owns repository merge enforcement

Repository checks, reviews, protected branches, and deployment/release rules remain an independent project boundary. Cortex completion evidence cannot silently bypass project-required merge controls.

## Provider-neutral target shape

```text
                         PROJECT
            requirements / code / tests / ADRs
              acceptance / SLOs / benchmarks
                            |
              +-------------+--------------+
              |                            |
              v                            v
        LIVE PROJECT                    FOSSIL
    current authoritative state      durable knowledge
                                     provenance/lineage
                                     knowledge graph
              |                            |
              +--------------+-------------+
                             v
                       bounded context
                             |
                             v
                     CORTEX V6 KERNEL
          +-----------------------------------+
          | state / generation / authority    |
          | routing / AssurancePlan           |
          | evidence binding / transitions    |
          +----------------+------------------+
                           |
                  RuntimeProvider
                           |
              +------------+------------+
              v                         v
   Microsoft Agent Framework       AWS AgentCore
          first                    later challenger
              |                         |
              +------------+------------+
                           |
          +----------------+------------------+
          v                v                  v
       LiteLLM          tools/effects      assurance
          |                                   |
       models                        tests/PBT/mutation
                                     TLA+/proofs/BDD
                                     benchmarks/chaos
          |                |                  |
          +----------------+---------+--------+
                                     v
                               evidence/results
                                     |
                                     v
                                  V6 gate
                         retry / blocked / complete
```

## Runtime portability invariant

No Microsoft-, Azure-, AWS-, AgentCore-, or Foundry-specific object may become authoritative Cortex state.

A Cortex task/work unit must retain the same meaning if its execution provider changes. Provider-specific capabilities may be exposed as optional runtime capabilities, but must not silently redefine the portable lifecycle/evidence semantics.

The exact `AgentRuntime`/`RuntimeProvider` methods are intentionally not frozen here. #10 must derive the smallest contract from observed #3 requirements rather than invent a general plugin framework.

## Core distinctions

### Semantic task state is not transcript

The system must retain explicit goals/constraints/accepted decisions/unresolved questions/completion criteria independently of conversational history.

### Working context is not durable knowledge

Working context is temporary, bounded material selected for a task. Protected semantic task state cannot be silently compacted away.

Durable knowledge/evidence may be supplied by FOSSIL, while live project sources provide current project facts. V6 owns bounded context composition, not the durable corpus.

### Execution result is not verification

The executor produces an effect/result. A separate verification/assurance path produces admissible evidence. Worker/model self-report is not completion evidence.

### Provider PASS is not lifecycle authority

A test runner, theorem prover, TLA+ checker, benchmark, reviewer, model, or managed runtime may return a result. Only V6's authoritative transition logic decides whether the currently required evidence permits a Cortex lifecycle transition.

### Component correctness is not composition correctness

A component is not considered protective merely because it exists or its unit tests pass. Critical acceptance tests must traverse the same composition path used by real work.

## First interfaces — still provisional

Only introduce interfaces required by the walking skeleton. Initial candidates remain:

- `RequirementState` / later exact snapshot identity;
- bounded context controller/provider seam;
- `WorkUnit`;
- controlled execution/effect boundary;
- independent verification boundary.

After #3 proves these semantics, later tracked candidates include:

- runtime-neutral `AgentRuntime` / `RuntimeProvider` (#10);
- `AssuranceObligation`, `AssurancePlan`, `AssuranceProvider`, `EvidenceReceipt` (#14);
- normalized model-provider boundary around LiteLLM (#19).

Do not build a generalized capability/package/plugin ecosystem around these names unless a later falsifiable case earns it.

## Initial invariants

1. A task cannot execute without stable task/requirement state.
2. Protected semantic state cannot disappear due to context compaction.
3. An effect cannot write outside its declared authority.
4. Verification cannot be satisfied by executor/model assertion alone.
5. Completion evidence binds to the exact authoritative input/work-unit version/generation.
6. Stale/mismatched results cannot complete a newer task state.
7. A system acceptance test traverses the production composition path.
8. External runtime/provider state cannot directly mutate authoritative V6 lifecycle state.
9. Current project facts cannot be overridden solely by stale FOSSIL memory.
10. Provider-specific identifiers cannot become required portable Cortex semantics.

## Assurance direction

V6 does not choose one universal methodology. Different assurance mechanisms answer different questions. #14 defines the common obligation/evidence boundary; #15 qualifies the kernel itself externally using multiple mechanisms where they independently attack different failure classes.

Likely methods include tests, BDD, stateful PBT, mutation/wiring mutants, TLA+/TLC, theorem-prover/SMT candidates, security analysis, benchmarks, fault injection, critiques, and later sealed qualification. Their exact task/risk routing policy remains open until measured.

## Agent topology direction

Interactive coding, delegated workers, planners/researchers, parallel workers, reviewers/critics, assurance specialists, maintenance agents, and evaluators should be expressed as roles/topologies over common work/authority/evidence primitives rather than separate Cortex products (#16).

## Context / knowledge-graph direction

The FOSSIL knowledge graph is a durable relationship/retrieval projection, not the Cortex brain or active task state. It may surface related requirements, ADRs, historical failures, invariants, prior evidence, proofs, tests, and benchmarks.

The actual context composition remains a bakeoff between project-only, FOSSIL-only, and hybrid providers (#17). Downstream task correctness and adversarial failures decide the role; retrieval metrics alone do not.

## Anti-circular bootstrap

The external development/CI pipeline must qualify V6 before V6 is trusted to autonomously route assurance for other projects. V6 cannot establish its own trust merely by orchestrating itself and reporting PASS.

## Anti-waste gate

#18 compares V6 against a serious conventional baseline: coding agent + project CI/review. V6 must materially justify its additional control/assurance complexity on consequential outcomes. A go/narrow/kill decision follows the benchmark.

## Architecture change rule

If a PR changes a durable boundary, authoritative state owner/writer, lifecycle transition, trust assumption, portability invariant, or evidence-admission rule, it must update this document or another durable design document and explain the change in its tracking issue.
