# Cortex V6 Roadmap

This file is a human-readable index of tracked work. GitHub issues remain the authoritative work items. The detailed durable handoff is `docs/V6_LOCKED_PLAN.md`; draft PR #20 carries the locked-plan documentation into `main`.

## P0 — bootstrap and first kernel proof

- #1 — bootstrap governance, durable docs, and traceability gate. **Bootstrap complete; branch enforcement remains #8.**
- #2 — establish ordinary SWE foundation and CI before kernel work.
- #3 — prove one real walking skeleton end to end.
- #4 — recover V4 stable task-state and context-preservation invariants.
- #8 — require docs/SWE gates through GitHub branch protection/rulesets.
- #9 — lock V6 as a portable engineering-assurance/lifecycle kernel over external agent runtimes.

## P1 — prove boundaries before broad autonomy

- #5 — qualify V5 donor components individually; V5 remains frozen reference/donor rather than a runtime target.
- #7 — encode SCC v2 failures as V6 adversarial/system tests.
- #10 — derive the runtime-neutral `AgentRuntime`/provider contract and portability invariant from real kernel needs.
- #11 — qualify Microsoft Agent Framework as the first runtime substrate.
- #13 — define project/V6/FOSSIL/runtime/model/assurance ownership contracts.
- #14 — define `AssurancePlan`, `AssuranceProvider`, and `EvidenceReceipt` contracts.
- #15 — qualify the V6 kernel externally with parallel assurance layers before trusting autonomous assurance routing.

## P2 — provider composition, routing, and falsification

- #6 — retire SSC v1 runtime seams without preselecting the context winner.
- #12 — prove AWS AgentCore can replace the first runtime without rewriting V6 authoritative semantics.
- #16 — express agent-driven development modes as routed roles/topologies over common primitives, not separate products.
- #17 — run live-project vs FOSSIL vs hybrid context composition bakeoff.
- #18 — benchmark V6 against conventional coding-agent + CI/review baselines and make a go/narrow/kill decision.
- #19 — integrate LiteLLM behind V6-owned semantic model seating/routing policy.

## Locked ownership summary

```text
PROJECT
  owns requirements/current artifacts/acceptance meaning

V6
  owns state/scope/routing/assurance obligations/evidence/transitions

FOSSIL
  owns durable knowledge/provenance/lineage/KG/retrieval projections

RUNTIME PROVIDER
  owns sessions/isolation/tool transport/runtime identity/telemetry

LiteLLM
  owns model/provider transport

ASSURANCE PROVIDERS
  execute method-specific checks and return evidence

GitHub/CI
  owns independent repository merge/release enforcement
```

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
#3 minimal walking skeleton
 |\
 | +--> #4 V4 state/context invariants
 | +--> #7 SCC v2 adversarial composition tests
 | +--> #13 ownership contracts
 | +--> #10 runtime-neutral contract
 |
 +----> #14 assurance/evidence contracts
          |\
          | +--> #15 external kernel assurance qualification
          | +--> #16 routed agent roles/topologies
 |
 #10 --> #11 Microsoft Agent Framework qualification
           |
           +--> #12 AWS AgentCore portability challenger
 |
 #4 + #13 --> #17 project/FOSSIL/hybrid context bakeoff
 |
 #10 + #13 --> #19 LiteLLM/model seating integration
 |
 #4 + #17 --> #6 SSC v1 retirement on the selected context path
 |
 #11 + #14 + #15 + #16 + #17 (+ #19 as needed)
           |
           v
#18 conventional-baseline comparison
           |
           v
      GO / NARROW / KILL
```

## Execution rule

The graph is not permission to build everything. Each later node is conditional on earlier evidence. #2 and #3 remain the immediate path. Do not attach Microsoft Agent Framework, AgentCore, FOSSIL, LiteLLM, a planner fanout, or a general assurance-provider framework to #3 merely because they appear later on the roadmap.

## Runtime portability rule

Microsoft Agent Framework is the first implementation substrate, not an authoritative Cortex state model. No Microsoft/Azure/AWS/AgentCore/Foundry identifier may become required portable Cortex semantics. #12 must prove that the same V6 work/evidence contract can run on AgentCore later without a Cortex lifecycle rewrite.

## Context rule

Do not call FOSSIL the settled V6 "search brain." Live project state is authoritative for current project facts. #17 compares project-only, FOSSIL-only, and hybrid context on downstream correctness, freshness, provenance, leakage, poisoning, latency/cost, and graceful degradation.

## Assurance rule

V6 does not pick one universal methodology. Tests, BDD, PBT, mutation, TLA+, theorem proving, security analysis, benchmarks, chaos/fault injection, critiques, and holdouts remain external mechanisms. #14 defines common obligation/evidence semantics; #15 uses multiple mechanisms to qualify V6 itself before autonomous routing is trusted.

## Backlog admission rule

Do not add a roadmap node because a capability sounds useful. A new issue that proposes architecture should identify:

1. the observed problem;
2. the simplest/conventional baseline;
3. evidence or experiment showing the gap;
4. alternatives/mature dependencies considered;
5. new failure modes introduced;
6. an acceptance test that can falsify the proposal.

Research may exist without a committed architecture boundary.

## Anti-waste rule

#18 is the explicit burden-of-proof gate. If V6 does not materially outperform a simpler coding-agent + project CI/review pipeline on consequential failures or review burden enough to justify added complexity, V6 must be narrowed or the extra mechanism removed.
