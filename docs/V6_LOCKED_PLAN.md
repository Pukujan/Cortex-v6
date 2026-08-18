# Cortex V6 Locked Plan and Session Handoff

**Status:** locked execution direction, still falsifiable at explicit qualification gates.  
**Tracking:** #9  
**Purpose:** this document is the durable handoff for the next planning/implementation session. It is intended to make the chat transcript unnecessary for resuming V6 work.

---

## 1. Executive summary

Cortex V6 is being reduced to a **small portable engineering-assurance and lifecycle kernel** that sits above mature agent/runtime/model/tooling systems instead of rebuilding those systems.

The kernel exists only to own semantics that must remain stable across agent frameworks, clouds, models, context providers, and assurance tools:

1. authoritative task/work lifecycle state;
2. exact requirement/work-unit/generation identity;
3. scope and authority grants;
4. task/risk/agent-topology routing;
5. required assurance obligations;
6. evidence admission and exact-version binding;
7. retry / blocked / verifying / complete transitions.

Everything else should remain external unless a measured failure forces a new kernel responsibility.

The initial runtime substrate will be **Microsoft Agent Framework**, selected because it is MIT-licensed and suitable for local/open-source research. V6 must not become coupled to Microsoft or Azure concepts. A runtime-neutral adapter boundary must make a later **AWS AgentCore** implementation possible without rewriting authoritative Cortex state.

**LiteLLM** remains the model/provider boundary. **FOSSIL** remains the durable knowledge/evidence/provenance/lineage system. Its knowledge graph and retrieval projections inform context and relevance but do not own current project truth or Cortex lifecycle state. **Pytest, Hypothesis/PBT, mutation frameworks, BDD, TLA+/TLC, theorem provers, security tools, benchmarks, chaos/fault injection, critics, and holdouts remain external assurance providers.**

The first implementation sequence remains deliberately smaller than this final target:

```text
#2 ordinary SWE foundation
        ↓
#3 one real minimal kernel walking skeleton
        ↓
#4 recover V4 state/context invariants
   +
#7 encode SCC v2 historical failures
        ↓
prove the kernel externally
        ↓
introduce provider/runtime/assurance boundaries only when earned
```

V6 must eventually be benchmarked against a serious conventional baseline: **coding agent + project CI/review**. If V6 does not materially reduce consequential failures, false completion, unauthorized effects, stale-result acceptance, or review burden enough to justify its complexity, the added mechanism must be narrowed or killed.

---

## 2. Why this plan exists

Earlier Cortex generations accumulated strong individual ideas but repeatedly suffered from one or more of these failures:

- too many products/planes before ordinary SWE foundations were universal;
- component correctness without production-path composition correctness;
- transcript/message history treated as semantic state;
- context corruption and compaction losing task truth;
- worker/model output being trusted too close to completion authority;
- provider/runtime concerns leaking into Cortex semantics;
- unclear ownership between Cortex, FOSSIL, the project, and execution infrastructure;
- architecture chosen before alternatives were falsified;
- sophisticated assurance mechanisms proposed before the basic kernel itself was independently qualified.

The V6 recovery rule is therefore subtractive:

> A mechanism does not enter Cortex merely because it is useful. It enters Cortex only if Cortex must own that semantic responsibility for the system to remain correct and portable.

Everything else should be delegated to mature external software.

---

## 3. Locked ownership model

### 3.1 Project owns WHAT must be true

The project is authoritative for current project meaning and current project artifacts:

- requirements;
- constraints;
- acceptance criteria;
- current source code;
- current tests;
- current configuration;
- current Git state;
- ADRs and architecture constraints;
- SLO/performance requirements;
- security requirements;
- project-specific benchmarks;
- project-specific policies;
- explicit human decisions.

Cortex may snapshot these items for a work generation, but Cortex does not silently redefine them.

A useful formulation is:

> The project says what must be achieved.

### 3.2 Cortex V6 owns CONTROL

V6 owns the operational semantics required to safely attempt work:

- `RequirementSnapshot` / equivalent exact input identity;
- `WorkUnit` identity;
- generation/version fencing;
- authoritative lifecycle state;
- read/write/capability authority for a work unit;
- risk/task classification used for routing;
- worker/reviewer/assurance topology selection;
- model seating semantics;
- `AssurancePlan` obligations;
- evidence admission and exact-version binding;
- retry, wait, blocked, verifying, complete transitions.

A useful formulation is:

> Cortex controls how work is attempted and what evidence is required before declaring success.

### 3.3 FOSSIL owns KNOWLEDGE

FOSSIL owns durable knowledge/evidence semantics, not active work lifecycle:

- immutable/original evidence where available;
- provenance;
- lineage;
- stable source/evidence identity;
- source-quality metadata;
- historical/reusable knowledge;
- claims and relationships;
- disagreement;
- revision/supersession;
- durable research context;
- project/domain/common memory packs;
- knowledge-graph projections;
- lexical/vector retrieval projections.

FOSSIL does **not** own:

- the current Cortex task state;
- a V6 work generation;
- whether a V6 task is complete;
- current live project source/config truth when the repository has changed since FOSSIL memory was captured.

A useful formulation is:

> FOSSIL tells Cortex what is known, where it came from, how it relates, and how durable evidence has evolved.

### 3.4 Runtime substrate owns EXECUTION INFRASTRUCTURE

The runtime substrate may provide:

- agent session mechanics;
- process/container/microVM execution;
- isolation/sandboxing;
- runtime identity/credentials;
- tool transport/gateway;
- provider-specific policy enforcement;
- telemetry;
- traces;
- runtime cancellation/termination;
- optional browser/code-interpreter/etc. capabilities.

For the first implementation this substrate is Microsoft Agent Framework. Later AWS AgentCore should be independently qualified behind the same V6 semantic boundary.

The runtime does **not** own the authoritative Cortex task merely because it has a session/thread ID.

### 3.5 LiteLLM owns MODEL TRANSPORT

LiteLLM remains responsible for model/provider transport and endpoint abstraction. Cortex may own semantic seating/routing decisions, but provider protocol details do not belong in Cortex task state.

Current selected target policy to preserve until evidence changes it:

- rank eligible models by strength;
- choose seats across vendors;
- probe failure ceiling: 3;
- normal retry ceiling: 30.

This policy is tracked separately in #19.

### 3.6 Assurance providers own METHOD-SPECIFIC EXECUTION

Assurance tools may execute:

- unit/integration/system tests;
- BDD scenarios;
- property-based/stateful tests;
- mutation tests;
- TLA+/TLC model checking;
- theorem proving/SMT;
- security/static analysis;
- benchmarks;
- chaos/fault injection;
- independent model critiques;
- sealed/hidden qualification.

They return evidence. They do not directly mutate Cortex lifecycle state.

### 3.7 GitHub/CI owns repository merge enforcement

GitHub branch protection, required status checks, reviews, CODEOWNERS, and deployment/release policy remain independent repository authorities. Cortex evidence must not silently bypass project-required merge controls.

---

## 4. Locked top-level architecture

```text
                         PROJECT
            requirements / code / tests / ADRs
              acceptance / SLOs / benchmarks
                            │
              ┌─────────────┴──────────────┐
              │                            │
              ▼                            ▼
        LIVE PROJECT                    FOSSIL
   current authoritative state       durable knowledge
                                     evidence/provenance
                                     lineage/history
                                     knowledge graph
                                     retrieval projections
              │                            │
              └──────────────┬─────────────┘
                             ▼
                       bounded context
                             │
                             ▼
                     CORTEX V6 KERNEL
          ┌───────────────────────────────────┐
          │ authoritative work/task state     │
          │ exact generation/version identity │
          │ scope / authority                 │
          │ task-risk-topology routing        │
          │ AssurancePlan                     │
          │ evidence binding                  │
          │ lifecycle transition gate         │
          └───────────────┬───────────────────┘
                          │
             RuntimeProvider / AgentRuntime
                          │
             ┌────────────┴─────────────┐
             ▼                          ▼
   Microsoft Agent Framework       AWS AgentCore
          FIRST                     LATER TEST
             │                          │
             └────────────┬─────────────┘
                          │
        ┌─────────────────┼─────────────────────┐
        ▼                 ▼                     ▼
     LiteLLM           tools/effects        assurance providers
        │                                      │
  models/providers                   Pytest / Hypothesis / mutation
                                     BDD / TLA+ / theorem proving
                                     security / benchmark / chaos
                                     critique / holdout
        │                 │                     │
        └─────────────────┴──────────┬──────────┘
                                     ▼
                               evidence/results
                                     │
                                     ▼
                                 CORTEX V6
                           retry / block / complete
                                     │
                                     ▼
                              GitHub/CI merge gates
```

This diagram is intentionally asymmetric: the project and FOSSIL provide information; runtimes execute; assurance providers produce evidence; only Cortex owns Cortex lifecycle transitions.

---

## 5. Runtime portability invariant

The primary cloud/runtime portability rule is:

> No Microsoft-, Azure-, AWS-, AgentCore-, or Foundry-specific object may become authoritative Cortex state.

A Cortex task must remain the same semantic task if execution moves between runtime providers.

Example:

```text
Cortex task T17 / generation 8
        │
        ├─ execution attempt A
        │      Microsoft session M123
        │
        └─ later execution attempt B
               AgentCore session A991
```

`M123` and `A991` are execution-resource identifiers. Neither is `T17`.

The runtime-neutral contract must be derived from real needs after #3. Candidate concepts are deliberately narrow:

```text
start / execute / cancel / status / evidence / terminate
```

Do not create a broad plugin SDK before a real adapter needs it.

Vendor capabilities such as Cedar policies, Azure-specific identity, managed browser, managed memory, special gateways, or vendor evaluators should be represented as optional capabilities rather than promoted into the universal V6 contract.

Tracked by #10, #11, #12.

---

## 6. Why Microsoft Agent Framework is first

The current implementation direction is to learn/build against Microsoft Agent Framework first because:

- it is MIT-licensed;
- it can be used locally;
- it supports a career/certification learning path without requiring V6 to depend on managed Azure hosting;
- it can act as an execution/orchestration substrate while V6 remains responsible only for its own control semantics;
- it avoids spending V6 effort rebuilding generic agent runtime infrastructure.

The decision is **Microsoft-first, not Microsoft-owned**.

Managed Microsoft Foundry may still be used for learning/deployment experiments later. It is not the authoritative basis of V6 state.

AWS AgentCore is the deliberate portability challenger. #12 exists specifically to prove or falsify the claim that the provider-neutral boundary is real.

If adding AgentCore requires redesigning V6's authoritative lifecycle model, the portability abstraction is wrong and must be revisited.

---

## 7. Agent-driven development modes: roles/topologies, not ten products

The production ecosystem contains several recurring agentic development patterns:

1. interactive/pair coding;
2. delegated implementation;
3. planning/research;
4. parallel/multi-agent development;
5. reviewer/critic;
6. specialist assurance;
7. maintenance/operations;
8. evaluation/benchmarking;
9. runtime/control-plane execution;
10. engineering-assurance meta-control.

V6 should **not** create ten subsystems for these.

Most are different role/topology combinations over common primitives.

Candidate actor roles:

```text
WORKER
PLANNER
RESEARCHER
REVIEWER / CRITIC
ASSURANCE
EVALUATOR
```

Examples:

### Simple bug fix

```text
worker
  ↓
project tests
  ↓
review
  ↓
completion gate
```

### High-risk concurrency change

```text
planner/researcher
       ↓
worker
       ↓
reviewer
       ↓
assurance obligations
  ├─ stateful PBT
  ├─ mutation
  ├─ TLA+/TLC
  └─ fault/replay tests
       ↓
evidence bundle
       ↓
V6 transition gate
```

### Architecture change

```text
research/planning
       ↓
ADR obligation
       ↓
worker
       ↓
production-composition test
       ↓
review/assurance
```

This is tracked by #16.

---

## 8. Assurance model

### 8.1 Do not choose one methodology religion

V6 should not globally choose TDD, BDD, PDD, SDD, TLA+, theorem proving, mutation testing, or holdouts as a universal methodology.

Different mechanisms answer different questions.

A practical mapping is:

| Mechanism | Primary question |
|---|---|
| Unit/TDD examples | Does this concrete behavior work? |
| BDD | Does user/domain-visible behavior match agreed examples? |
| PBT/stateful PBT | Does an invariant survive many generated values/sequences? |
| Mutation | Would the tests/evidence notice a deliberate fault? |
| Wiring/architecture mutants | Can production composition bypass a protective component? |
| TLA+/TLC | Do declared state-machine safety/liveness properties survive explored interleavings? |
| Theorem proving/SMT | Does a formalized proposition follow from declared assumptions? |
| Security/static analysis | Are known vulnerability classes/policy violations present? |
| Benchmark | Does measured correctness/performance meet a threshold? |
| Chaos/fault injection | Does the real implementation survive failures/recovery? |
| Independent critic/reviewer | Can another path identify defects/assumption errors? |
| Hidden/sealed qualification | Did development overfit visible checks? |

No one row proves total software correctness.

### 8.2 V6 owns the assurance decision, not the tools

The planned abstractions are:

```text
AssuranceObligation
AssurancePlan
AssuranceProvider
EvidenceReceipt
```

Example:

```text
AssuranceObligation
  kind: concurrent_safety
  property: stale_generation_cannot_commit
  requirement_version: R17@12
  work_unit: W81
  generation: 44

Provider
  TLC

EvidenceReceipt
  provider/version
  model/spec hash
  exact input identity
  result
  artifacts
  execution metadata
```

A `PASS` receipt does not directly set `COMPLETED`. V6 validates whether the receipt is expected, current, admissible, correctly bound, and sufficient together with other required obligations.

Tracked by #14.

### 8.3 V6 itself must be externally qualified first

This is the anti-circular bootstrap rule:

> The development pipeline used to qualify the V6 kernel must exist independently of V6 orchestration.

Before autonomous assurance routing is trusted, V6 should be attacked externally with:

- strict typing/lint/import checks;
- unit/integration/system tests;
- Hypothesis/stateful PBT;
- domain mutants;
- wiring/architecture mutants;
- TLA+/TLC when retry/replay/concurrency semantics appear;
- proof candidates for narrow formalizable predicates;
- fault/crash/replay tests;
- historical SCC v2 negative controls;
- automated benchmarks;
- later sealed qualification where justified.

Tracked by #15.

---

## 9. Core kernel invariants to preserve

The existing V6 walking-skeleton invariants remain the foundation:

1. no execution without stable task/requirement state;
2. transcript is not authoritative task truth;
3. protected semantic state cannot silently disappear under context pressure;
4. effects cannot exceed declared authority;
5. worker/model assertion alone cannot satisfy verification;
6. completion evidence binds to the exact authoritative input/work-unit generation;
7. stale/mismatched results cannot complete newer state;
8. production acceptance must traverse the same composition path used by real work.

As V6 gains retries/concurrency, candidate additional properties include:

- at most one authoritative completion for a generation;
- old generations cannot overwrite newer state;
- retry/replay cannot silently double-apply non-idempotent effects;
- evidence generated before authoritative input changes cannot authorize the new generation;
- reviewer/assurance actors cannot gain worker mutation authority unless explicitly granted;
- provider/runtime failure cannot directly advance lifecycle state.

These properties should be expressed in the most appropriate assurance mechanism rather than forced into one test style.

---

## 10. Context and knowledge graph plan

### 10.1 The knowledge graph is not the Cortex brain

The FOSSIL knowledge graph belongs to FOSSIL as a projection/index over durable knowledge and lineage.

It may represent relationships such as:

```text
Requirement R17
 ├─ implemented_by → PaymentService
 ├─ constrained_by → ADR-004
 ├─ verified_by → test_double_capture
 ├─ verified_by → TLA:AtMostOnce
 └─ supersedes → R11

PaymentService
 ├─ depends_on → Ledger
 ├─ modified_by → commit abc123
 └─ previously_failed → Bug #918

EvidenceReceipt E88
 ├─ verifies → R17
 ├─ generated_by → TLC
 └─ bound_to → commit abc123
```

This can help Cortex discover affected requirements, historical failures, prior assurance artifacts, ADRs, proofs, tests, and benchmarks.

But graph membership/rank does not grant authority.

### 10.2 Freshness rule

If FOSSIL says a component uses Redis but the live repository now uses Postgres, the live project source wins for current project state.

FOSSIL should preserve historical/supersession lineage rather than silently replace it.

### 10.3 Context architecture remains a measured question

The earlier statement "FOSSIL should be V6's search brain" was too strong. The current serious alternatives are:

A. project-only current context;  
B. FOSSIL-only durable retrieval;  
C. hybrid live project + FOSSIL.

#17 must compare these on downstream correctness and adversarial failure cases, not just MRR/recall.

The expected but unproven hypothesis is:

> live project sources are authoritative for current project state; FOSSIL contributes durable history/research/lineage/provenance where that improves the task; V6 composes bounded context.

This remains falsifiable until #17 runs.

---

## 11. FOSSIL ingestion guidance for this transcript

The transcript may be ingested into FOSSIL as **research/decision-lineage evidence**, not as unquestioned architectural truth.

Recommended treatment:

```text
Research question:
How should V6 compose project requirements, portable agent runtimes,
model providers, FOSSIL, heterogeneous assurance systems, and lifecycle authority?

Current candidate/decision:
small portable V6 control kernel over external subsystems

Evidence classes:
- repository evidence from V4/V5/SCC v2/V6/FOSSIL;
- production-platform research on AWS/Microsoft/GitHub/OpenAI/Anthropic;
- formal-method/PBT/mutation/evaluation research;
- failed/overstated earlier hypotheses and their corrections.

Status:
locked execution direction with explicit falsification gates

Important superseded claim:
"FOSSIL is the V6 search brain" is not accepted as settled architecture.

Current context hypothesis:
live project + FOSSIL hybrid is plausible, but #17 must test it.
```

The transcript contains useful decision provenance because it records alternative theories, rejected assumptions, and why the current split exists. FOSSIL should preserve that lineage rather than flatten the entire conversation into CURRENT_BEST claims.

For current implementation authority, prefer this repository's issues/docs over conversational prose.

---

## 12. V5 / V4 / SCC v2 lineage status

### V5

V5 is frozen as a reference/donor. Do not attempt architecture rehabilitation. Individual code may be inspected/qualified only if a current issue demonstrates it beats mature external alternatives.

The old V5 runtime composition is not the target V6 runtime.

### V4

V4 remains a behavioral reference for:

- stable semantic task state separate from transcript;
- bounded context;
- protected spans/state;
- context compaction/offload behavior;
- fail-closed preservation checks;
- selected action/state invariants.

#4 owns this recovery.

### SCC v2

SCC v2 is primarily a negative-control/failure corpus. Its strongest lesson is:

> Correct components are not a correct system. The system property lives in production composition.

#7 turns historical failure modes into adversarial V6 system tests.

---

## 13. Model seating / LiteLLM plan

Model transport should remain below a narrow V6 model boundary.

Current selected routing target:

```text
rank eligible models by strength
        ↓
choose cross-vendor seats
        ↓
probe: up to 3 failed retries
        ↓
normal retry ceiling: 30
        ↓
retry / switch / wait according to V6 lifecycle semantics
```

LiteLLM may provide operational transport/routing features, but those should not silently replace Cortex semantic policy.

The same model request semantics should remain valid if the runtime substrate changes from Microsoft Agent Framework to AgentCore.

Tracked by #19.

---

## 14. External production precedent and what V6 must not rebuild

Current production systems already provide substantial portions of generic agent infrastructure:

- coding agents can edit code, run tests, and create PRs;
- GitHub provides CI, protected branches, reviews, security checks, and deployment gates;
- AWS AgentCore provides managed runtime/isolation, gateways, identity, policy enforcement, traces, evaluations, and optional formal-policy checking;
- Microsoft Agent Framework/Foundry provide agent/workflow primitives, evaluator abstractions, managed deployment options, red teaming, approvals, and observability;
- LiteLLM provides multi-provider model access/routing abstractions;
- established formal/test tools already solve method-specific assurance execution.

Therefore V6 should not rebuild:

- sandbox/container infrastructure;
- cloud agent hosting;
- Git;
- CI;
- IAM;
- theorem provers;
- model checkers;
- mutation frameworks;
- tracing platforms;
- generic vector databases;
- provider protocol gateways.

The remaining hypothesis V6 must earn is the value of a small **software-engineering assurance controller** that binds exact work state to required heterogeneous evidence.

---

## 15. The anti-waste benchmark

The strongest alternative to V6 is not "no agents." It is a modern conventional pipeline:

```text
coding agent
    ↓
project tests/lint/typecheck
    ↓
GitHub CI/security checks
    ↓
human/AI review
    ↓
protected merge
```

V6 must be compared with that baseline.

#18 defines three contenders:

A. conventional coding agent + project CI/review;  
B. coding agent + broad static assurance stack without V6 control semantics;  
C. V6 + same agent/runtime/CI + task/property-derived assurance + exact evidence binding.

Task classes must include both cases where V6 might help and cases where it should lose on overhead:

- ordinary bug fix;
- user-visible behavior;
- authorization/security;
- state/retry logic;
- concurrency;
- migration;
- performance;
- architecture-boundary change.

Primary measures include:

- escaped defects;
- false completion;
- stale-result acceptance;
- unauthorized effects;
- security failures;
- human review effort;
- time;
- inference/compute cost;
- operational/config/code complexity;
- graceful degradation.

If V6 does not materially improve consequential outcomes, narrow or kill the added mechanism.

---

## 16. Issue map after this handoff

### Existing foundation

- **#1** bootstrap governance/docs/traceability — completed bootstrap baseline.
- **#2** ordinary SWE foundation before kernel work — immediate implementation priority.
- **#3** one real V6 walking skeleton — first kernel proof.
- **#4** recover V4 state/context invariants.
- **#5** qualify V5 donor components individually — V5 remains frozen reference/donor.
- **#6** retire SSC v1 runtime seams without preselecting context winner — updated to depend on #17.
- **#7** SCC v2 failure corpus as production-path adversarial tests.
- **#8** make docs/SWE checks required GitHub branch protections.

### Locked-plan issues

- **#9** parent decision: portable engineering-assurance kernel over external runtimes.
- **#10** runtime-neutral `AgentRuntime`/provider contract and portability invariant.
- **#11** Microsoft Agent Framework first-runtime qualification.
- **#12** AWS AgentCore replacement/portability proof.
- **#13** project/V6/FOSSIL/runtime/model/assurance ownership contracts.
- **#14** `AssurancePlan` / `AssuranceProvider` / `EvidenceReceipt` contracts.
- **#15** externally qualify V6 kernel with parallel assurance layers.
- **#16** agent-driven development modes as roles/topologies over common primitives.
- **#17** live-project vs FOSSIL vs hybrid context bakeoff.
- **#18** V6 vs conventional coding-agent+CI automated benchmark/kill criterion.
- **#19** LiteLLM integration behind V6-owned model seating policy.

---

## 17. Planned dependency shape

The exact issue graph may be refined next session, but the intended ordering is:

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
 | +--> #10 runtime-neutral contract (only from observed needs)
 |
 +----> #14 assurance/evidence contracts
          |
          +--> #15 kernel assurance qualification
          |
          +--> #16 routed agent roles/topologies
 |
 #10 --> #11 Microsoft Agent Framework qualification
           |
           +--> #12 AWS AgentCore portability challenger
 |
 #4 + #13 --> #17 project/FOSSIL/hybrid context bakeoff
 |
 #10 + #13 --> #19 LiteLLM/model seating integration
 |
 #11 + #14 + #15 + #16 + #17 (+ #19 as needed)
           |
           v
#18 V6 vs conventional pipeline benchmark
           |
           v
      GO / NARROW / KILL
```

Do not implement later nodes merely because they appear in this graph. Dependencies identify where a decision can be tested; they are not permission to skip earlier evidence.

---

## 18. Immediate next-session starting point

Do **not** reopen the entire architecture debate first.

Start by reading, in order:

1. `docs/V6_LOCKED_PLAN.md` (this file);
2. #9 parent decision;
3. #2 and the current `agent/swe-foundation` branch/PR state;
4. #3 walking skeleton;
5. #4 and #7 for the first invariant/adversarial expansion;
6. only then #10/#13/#14 for provider boundaries.

The immediate implementation work remains #2 unless its branch/PR has already completed.

After #2, #3 must stay intentionally tiny. Do not attach Microsoft Agent Framework, AWS AgentCore, FOSSIL, LiteLLM, planner fanout, dynamic risk routing, or a general assurance-provider framework merely to make #3 look production-complete. #3 exists to prove the irreducible kernel control semantics first.

Once #3 survives, the later external-runtime architecture can be introduced against something already known to enforce the essential lifecycle/authority/evidence invariants.

---

## 19. Things that are locked versus still open

### Locked execution direction

- V6 is a small control/assurance/lifecycle kernel, not a general agent runtime platform.
- Use mature external agent/runtime infrastructure.
- Microsoft Agent Framework is the first local/open-source runtime substrate to qualify.
- V6 must remain portable enough to add AWS AgentCore later without rewriting authoritative Cortex semantics.
- LiteLLM remains the model/provider boundary.
- FOSSIL owns durable knowledge/provenance/lineage; its graph is not Cortex lifecycle state.
- Project owns current requirements/current project artifacts/acceptance meaning.
- Assurance tools are external providers; V6 owns obligation/evidence/transition semantics.
- GitHub/CI remains an independent merge enforcement layer.
- V5 remains frozen donor/reference.
- V6 must be benchmarked against a serious simpler baseline.

### Explicitly still open/falsifiable

- exact minimal methods on `AgentRuntime`;
- whether Microsoft Agent Framework creates unacceptable coupling in practice;
- whether AgentCore can satisfy the same semantic contract cleanly;
- exact `AssurancePlan` schema;
- exact task/risk routing policy;
- which tasks require BDD/PBT/mutation/TLA+/proofs/etc.;
- theorem-prover choice(s);
- whether a sealed evaluator needs its own repository/authority;
- project-only vs FOSSIL-only vs hybrid context by task class;
- how much knowledge-graph context actually improves downstream work;
- which V5 donor pieces, if any, remain worth reusing;
- whether V6 beats the simpler conventional baseline enough to continue.

This distinction is important: locking the execution direction does not convert every unresolved mechanism into architecture truth.

---

## 20. One-sentence system definition

> **Cortex V6 is a small provider-independent software-engineering control kernel that snapshots what a project requires, scopes and routes work through external agent runtimes, requires task-appropriate independent assurance evidence, binds that evidence to the exact work generation, and alone controls the Cortex lifecycle transition while FOSSIL supplies durable knowledge/provenance and GitHub/CI retains repository merge authority.**

That sentence should remain difficult to expand. If a future feature cannot be justified as necessary to preserve those control semantics, it probably belongs outside the kernel.
