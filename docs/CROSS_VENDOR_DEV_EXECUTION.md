# Cross-vendor development execution while V6 is under construction

**Status:** operational development runbook only. This does not implement #19 and does not change the locked #2 -> #3 -> #4/#7 integration order.

## Purpose

Cortex V5 is retired. V5 may be consulted only as historical donor/reference evidence for methodology, model ranking, seating mechanics, and failure lessons. No live V6 execution path should depend on the V5 runtime.

Until V6 has earned and implemented its own model/runtime boundary, cross-vendor coding, test-writing, review, and research that require a repository-aware frontier agent use OpenCode CLI as an external execution shell over the LiteLLM-compatible CKFF model boundary.

The temporary development flow is:

```text
live Cortex-v6 repository + relevant durable context
                    |
                    v
current task/risk/methodology policy
                    |
                    v
qualified cross-vendor seat selection
                    |
                    v
pre-granulated task packet
                    |
                    v
OpenCode CLI -> explicit LiteLLM model seat
                    |
                    v
workspace change / tests / research / critique
                    |
                    v
project tests + independent assurance + GitHub/CI
```

OpenCode is not authoritative Cortex state. LiteLLM is model transport. FOSSIL is not active task state. Project tests and later V6 evidence admission remain the completion authority.

## Ownership split

- **Live project:** current requirements, source, tests, config, ADRs, acceptance meaning, and Git state.
- **FOSSIL:** durable research, provenance, lineage, historical failures, prior evidence, and reusable knowledge. Current live repository state wins conflicts about present project facts.
- **Cortex/V6 policy:** task/risk classification, role/topology choice, model-seat eligibility/ranking, retry/switch decisions, evidence requirements, and later lifecycle transitions.
- **OpenCode:** temporary repository-aware coding/research/reviewer execution shell.
- **LiteLLM/CKFF:** provider/model transport only.
- **Project assurance/GitHub:** deterministic checks, review, CI, and merge authority.

## Canonical development inference contract: 600 seconds

For the V6 cross-vendor development lane, keep the inference-timeout contract deliberately simple:

- **one model request ceiling: 600 seconds**;
- OpenCode's CKFF/LiteLLM provider timeout is configured to **600000 ms**;
- LiteLLM's request timeout is configured to **600 seconds**;
- compatibility bridges must not introduce shorter per-model attempt deadlines;
- an OpenCode/LiteLLM/route build that terminates a valid request earlier than this contract is **unqualified for the V6 development lane** rather than becoming a new Cortex timeout policy.

The selected development route is the CKFF endpoint qualified for the 600-second envelope. Lower-timeout backup routes may exist operationally, but they are not interchangeable members of this V6 development contract and must not be selected automatically beneath Cortex/OpenCode.

Streaming remains preferred for long generations because it avoids idle-connection behavior, but streaming does not create a second semantic timeout value. The model request still has the same 600-second ceiling.

Local tool/subprocess/test timeouts may exist for their own deterministic operations. They are not model-seat deadlines and must not be reported as model capability failures.

### Qualification rule

Before relying on an OpenCode build for this lane, run a controlled qualification proving that its configured provider request can continue beyond any previously observed hidden ~300-second client cutoff and remains bounded by the 600-second contract. If the installed OpenCode version fails earlier, reject/upgrade/fix that client for this lane; do not encode the observed defect as a new 240- or 300-second Cortex policy.

## Exact model identity; no hidden cross-model fallback

A Cortex/bootstrap seating decision must remain observable end to end.

- Every summon names the exact selected LiteLLM model seat.
- The compatibility bridge must default to **no cross-model fallback**.
- LiteLLM may perform transport mechanics that preserve the same logical model identity, but it must not silently substitute a different model/vendor for the selected seat.
- If the selected model fails, the result returns to the Cortex/bootstrap seating controller.
- The controller decides whether to retry the same seat or switch to the next ranked cross-vendor seat.
- Any response metadata that reports a different actual model than the requested seat is rejected as invalid seating evidence unless that substitution was explicitly requested for a separate experiment.

This boundary matters because hidden provider fallback would corrupt model ranking, vendor-diversity, retry, failure, cost, and assurance evidence.

## Seating methodology while V6 is built

Reuse V5's **methodology** as donor evidence, not its runtime implementation or every historical constant.

The bootstrap/V6 target policy currently preserved by issue #19 is:

1. derive eligibility from the task, risk, role, and methodology;
2. rank eligible models by current strength/evidence;
3. select seats across independent vendors;
4. treat the first/health-recovery attempts as probes;
5. switch a seat after **3 probe failures**;
6. use a **30 normal-retry ceiling** when normal retry semantics apply;
7. record retry/switch outcomes separately from transport failures;
8. never count a shared route/client timeout as independent evidence that each model is incapable.

V5's older continuous-failure threshold is donor history, not V6 policy. #19 must implement and mechanically test the V6-native 3-probe / 30-normal contract when its entry gates are satisfied.

## Granulation rule

The controller/human prepares the granule **before** OpenCode receives it. Do not give a frontier coding agent an unbounded issue such as "implement the whole subsystem."

Each packet should contain:

```text
TASK / WORK UNIT / GENERATION OR REPO REF
ROLE: worker | test-writer | reviewer | researcher | evaluator
OBJECTIVE: one bounded outcome
AUTHORITATIVE INPUTS: exact issue/requirement/current repo refs
FOSSIL CONTEXT: only relevant durable facts with provenance
AUTHORIZED SCOPE: exact workspace/files/tools/effects
NON-GOALS: explicit exclusions
ACCEPTANCE: observable check for this granule
REQUIRED EVIDENCE: diff/tests/research/critique to return
MODEL SEAT: exact selected LiteLLM model
REQUEST CEILING: 600 seconds
STOP CONDITION: ambiguity, missing authority, prerequisite failure, or inability to finish the current model turn inside the request contract
HANDOFF: facts/checkpoint required by the next granule
```

A granule should normally change or answer one thing and have an obvious verification boundary. A longer engineering job proceeds through multiple bounded granules and model/tool turns rather than one recursively widening prompt.

## Role mapping

Use OpenCode as an execution shell, not an autonomous recursive organization.

- `worker` / `test-writer`: mutating coding agent in an authorized isolated workspace.
- `reviewer` / `researcher` / `evaluator`: non-mutating/read-oriented agent; allow web/repository research as needed but do not grant write authority by convenience.

For independent cross-vendor critique or evaluation, use seats from different vendors. For multiple mutating workers, give each seat an isolated worktree/workspace; never point multiple workers at one mutable checkout.

Disable or avoid recursive subagent fan-out and doom-loop recovery for this temporary path. Cortex/human granulation chooses the next bounded packet rather than allowing an execution agent to recursively widen the task.

## Seating donor evidence

V5's measured seating research may be reused as **donor evidence only**, not as V6 runtime code or permanent truth. Its last recorded five-vendor frontier prior was:

1. `grok-4.6` — xAI
2. `gpt-5.6-sol` — OpenAI
3. `kimi-k3` — Moonshot
4. `qwen3.8-max` — Alibaba
5. `gemini-3.6-flash` — Google

Before each consequential cross-vendor run, intersect any prior with the live LiteLLM catalog, model health, task suitability, vendor independence, and newer measured evidence. #19 still owns the eventual V6-native seating contract and must qualify it independently.

## What is deliberately not implemented yet

This runbook does **not** add a V6 LiteLLM client, model router, OpenCode dispatcher module, runtime adapter, or lifecycle integration. Doing that now would bypass the locked dependency gates.

When #19's entry gates are satisfied, its implementation should derive the V6 transport contract from current V6 needs and this operational evidence. It must not copy the retired V5 runtime wholesale.

## Resume rule

Any agent resuming Cortex V6 should read this file together with `docs/V6_LOCKED_PLAN.md` and issue #19 before doing cross-vendor frontier-agent work. Treat V5 as frozen historical evidence only.