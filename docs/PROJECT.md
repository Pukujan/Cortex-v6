# Cortex V6 Project Charter

## Purpose

Cortex V6 exists to recover the strongest proven behaviors of earlier Cortex work while removing accidental coupling, context corruption, architecture that has not earned its complexity, and runtime/provider responsibilities that mature software can already supply.

V6 is a **subtractive recovery program**. The default decision for a new Cortex mechanism is **do not add it** until a current failure demonstrates why Cortex itself must own that semantic responsibility.

The locked execution direction is tracked by #9 and documented in `docs/V6_LOCKED_PLAN.md`: V6 is a small provider-independent software-engineering control/assurance kernel over external agent runtimes, model providers, knowledge systems, assurance tools, and repository gates.

## Immediate success criterion

The first executable milestone remains exactly one real path:

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

This milestone deliberately does **not** require Microsoft Agent Framework, AWS AgentCore, FOSSIL, LiteLLM, dynamic assurance routing, or multi-agent fanout. The irreducible Cortex semantics must be proven first.

## Locked system responsibility

### Project owns WHAT must be true

Current requirements, constraints, source/tests/config, acceptance criteria, ADRs, SLO/security/performance requirements, project-specific benchmarks/policy, and explicit human decisions.

### Cortex V6 owns CONTROL

Authoritative work/task lifecycle state, exact requirement/work-unit/generation identity, scope/authority grants, task/risk/topology routing, model seating semantics, assurance obligations, evidence binding/admission, and lifecycle transitions.

### FOSSIL owns KNOWLEDGE

Durable evidence, provenance, lineage, source-quality metadata, historical/reusable knowledge, disagreement/supersession, and knowledge-graph/retrieval projections. FOSSIL does not own active Cortex task state.

### Runtime substrate owns EXECUTION INFRASTRUCTURE

Agent sessions, sandbox/isolation, tool transport, runtime identity/credentials, telemetry/traces, and provider-specific policy mechanisms. Microsoft Agent Framework is the first substrate to qualify; AWS AgentCore is the later portability challenger.

### LiteLLM owns MODEL TRANSPORT

Provider/model endpoint transport remains separate from Cortex semantic model seating/routing policy.

### Assurance providers own METHOD EXECUTION

Test frameworks, BDD/PBT/mutation, TLA+/TLC, theorem provers, security analysis, benchmarks, chaos/fault tools, critics, and holdouts return evidence rather than owning Cortex completion.

### GitHub/CI owns repository merge enforcement

Required checks, reviews, protected branches, and release/deployment controls remain independent project authorities.

## Non-negotiable invariants

1. The project/human owns project scope, requirements, and acceptance meaning.
2. Conversation/transcript is not authoritative task truth.
3. Stable task/requirement semantics are represented separately from working context.
4. Consequential effects require explicit authority.
5. Working context is bounded and protected semantic state cannot be silently dropped.
6. Model/worker output is not verification evidence by itself.
7. Completion requires evidence bound to the exact task/work-unit/generation version.
8. Stale attempts/results cannot advance newer authoritative state.
9. Durable knowledge belongs to FOSSIL; operational task state belongs to Cortex.
10. Component/unit correctness never substitutes for composition correctness.
11. External runtime/provider sessions cannot directly mutate authoritative Cortex lifecycle state.
12. No Microsoft-, Azure-, AWS-, AgentCore-, or Foundry-specific identifier may become required authoritative portable Cortex state.
13. Current live project facts cannot be overridden solely by stale durable memory.
14. Assurance-provider PASS does not directly imply Cortex completion.

## Explicit non-goals

V6 does not build its own substitutes for:

- generic agent hosting/runtime infrastructure;
- cloud sandbox/container/microVM infrastructure;
- IAM/identity systems;
- Git or CI;
- model-provider protocols/gateways;
- theorem provers/model checkers;
- mutation frameworks;
- BDD/PBT frameworks;
- generic benchmark runners;
- tracing platforms;
- vector/graph database infrastructure.

V6 also does not currently commit to separate Cortex products for:

- risk tiering;
- phase planning;
- decomposition/granularity;
- methodology classification;
- PDD/TDD/BDD/SDD strategy products;
- formal-method products;
- arbitration products;
- capability registries/package managers;
- autonomous learning;
- one subsystem per agent role;
- a universal plugin architecture.

Tracked narrow contracts such as runtime portability (#10), assurance/evidence (#14), and routed agent roles/topologies (#16) must earn their exact shape through implementation pressure and tests.

## Runtime direction

### First substrate: Microsoft Agent Framework

Use Microsoft Agent Framework as the first local/open-source agent runtime substrate after the minimal kernel path proves its own control semantics. It is an implementation dependency behind a provider-neutral boundary, not Cortex's state model.

### Later portability challenger: AWS AgentCore

#12 must run the same V6 work/evidence semantics through AgentCore without requiring a rewrite of authoritative Cortex lifecycle state. If that cannot be done cleanly, the runtime-neutral abstraction must be reconsidered.

### Model access: LiteLLM

LiteLLM remains the provider/model transport boundary. Current selected target seating policy is tracked in #19: strength-ranked eligible models, cross-vendor seats, 3 probe failures, 30 normal retries.

## Assurance direction

V6 does not select one universal development methodology. Different task/risk/property classes may require different combinations of tests, BDD, stateful PBT, mutation, TLA+, formal proof, security analysis, benchmarks, chaos/fault injection, critique, or holdout.

#14 defines common assurance-obligation/evidence semantics. #15 qualifies V6 itself using external assurance before V6 is trusted to autonomously route such methods for other projects.

## Context / FOSSIL direction

Do not assume FOSSIL is the sole search/context brain. Live project artifacts are authoritative for current project state. FOSSIL supplies durable history/evidence/provenance/lineage and knowledge-graph/retrieval signals.

#17 must compare project-only, FOSSIL-only, and hybrid context composition on downstream task correctness and adversarial failures. #6 now depends on that result before completing SSC v1 retirement.

## Lineage use

### SSC v1

Legacy reference/provider only. V6 must ultimately run with SSC v1 unavailable. Do not treat SSC prose/corpus as automatically authoritative durable knowledge.

### SCC v2

Negative-control source. Its failure reports become V6 adversarial/system tests where applicable.

### Cortex V4

Behavioral reference for stable task state, bounded context, protected spans, action gates, replay/fencing, and other behaviors independently shown useful.

### Cortex V5

**Frozen reference/donor.** Do not attempt runtime/architecture rehabilitation. Reuse is per-component and evidence-based only when a current V6 issue shows the donor beats mature external alternatives for the required capability.

### FOSSIL

Durable knowledge/evidence/provenance/lineage service. Its graph/retrieval projections may inform context and assurance relevance but do not own active task state or current project truth.

## Build order

### Immediate foundation

1. #1 governance/docs gate bootstrap.
2. #2 ordinary SWE foundation.
3. #3 one real minimal walking skeleton.
4. #4 recover V4 state/context invariants.
5. #7 encode SCC v2 failures as adversarial production-composition tests.

### Earned control/provider boundaries

6. #13 make ownership contracts explicit.
7. #10 derive the minimal runtime-neutral contract from observed kernel needs.
8. #14 define assurance obligations/providers/evidence receipts.
9. #15 externally qualify the kernel with parallel assurance layers.
10. #11 qualify Microsoft Agent Framework as first runtime substrate.

### Composition and portability

11. #16 represent agent-development modes as roles/topologies over common primitives.
12. #17 run project/FOSSIL/hybrid context bakeoff.
13. #19 integrate LiteLLM behind V6-owned semantic seating policy.
14. #6 finish SSC v1 retirement using the selected context path.
15. #12 qualify AWS AgentCore as a replacement runtime.
16. #18 compare V6 against conventional coding-agent + CI/review baselines and make a go/narrow/kill decision.

#5 remains available for narrowly qualifying any V5 donor component that still has a demonstrated need after mature dependencies are considered.

Expansion beyond this list requires its own tracked evidence.

## Anti-circular bootstrap rule

The external software-engineering pipeline must be able to qualify the V6 kernel before V6 itself is trusted to orchestrate project assurance. V6 cannot establish trust by merely asking itself to report that it passed.

## Anti-waste rule

V6 must eventually beat a serious simpler baseline on consequential outcomes. #18 explicitly compares V6 with conventional coding-agent + CI/review approaches. If added Cortex mechanisms do not materially reduce important failures or review burden enough to justify their complexity/cost, they must be narrowed or removed.
