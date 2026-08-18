# Cross-vendor development execution while V6 is under construction

**Status:** temporary external-engineering runbook only. This does not implement #19, does not make OpenCode part of authoritative V6 state, and does not change the #2 -> #3 -> #4/#7 minimal-kernel integration order.

**Governance:** fresh-session audit #25 governs this runbook. OpenCode bootstrap qualification is tracked by #33; external-data authority by #30; LiteLLM transport alignment by `Pukujan/litellm-ckff-ops#24`; seating/retry donor qualification by #31.

## Purpose

Cortex V5 is retired. V5 may be consulted only as historical donor/reference evidence for methodology, model ranking, seating mechanics, and failure lessons. No live V6 execution path should depend on the V5 runtime.

Until V6 has earned and implemented its own model/runtime boundary, repository-aware frontier-agent work may use OpenCode CLI as an **external execution shell** over the LiteLLM-compatible CKFF boundary.

OpenCode exists here to execute one bounded packet. It does not decide what the project is, what Cortex state means, which requirement is authoritative, whether work is complete, or what the next recursive task should become.

The temporary development flow is:

```text
live Cortex-v6 repository + explicitly approved durable context
                    |
                    v
human/bootstrap task-risk-methodology policy
                    |
                    v
qualified exact model seat
                    |
                    v
pre-granulated task packet + explicit egress/mutation authority
                    |
                    v
OpenCode CLI -> exact LiteLLM model
                    |
                    v
isolated workspace change / tests / research / critique
                    |
                    v
independent project checks + review + GitHub/CI
                    |
                    v
bootstrap controller decides next granule / retry / seat switch
```

## OpenCode is allowed to be

- a repository-aware **worker/test-writer** for one bounded mutation packet in an isolated authorized workspace;
- a **reviewer/researcher/evaluator** for one bounded read-oriented packet;
- a tool-using shell that can inspect authorized repository state, run authorized commands, and return a diff/test/research/critique artifact;
- a temporary bootstrap implementation detail while V6 itself is not yet trusted to orchestrate this work.

## OpenCode is not allowed to be

OpenCode is **not**:

- authoritative Cortex task, requirement, work-unit, generation, lifecycle, or completion state;
- the planner-of-record for an unbounded project or issue;
- permission to recursively decompose/widen work without returning control to the bootstrap controller;
- a hidden model router or cross-vendor fallback authority;
- permission to mutate the main/shared checkout from multiple workers;
- permission to read or transmit files outside the packet's explicit read/egress authority;
- a substitute for project tests, independent review, assurance, or GitHub/CI;
- a source of truth merely because the model says a task is done;
- native #19 implementation, a V6 `AgentRuntime`, or a permanent OpenCode dependency.

## Ownership split

- **Live project:** current requirements, source, tests, config, ADRs, acceptance meaning, and Git state.
- **FOSSIL:** durable research, provenance, lineage, historical failures, prior evidence, and reusable knowledge. Current live repository state wins conflicts about present project facts.
- **Bootstrap/Cortex policy:** task/risk classification, role/topology choice, model-seat eligibility/ranking, retry/switch decisions, evidence requirements, and later lifecycle transitions.
- **OpenCode:** temporary repository-aware execution shell only.
- **LiteLLM/CKFF:** exact-model transport only for this lane.
- **Project assurance/GitHub:** deterministic checks, review, CI, and merge authority.

## Entry gates for live external-model use

### Controlled qualification fixtures

Sanitized/non-sensitive qualification fixtures may be used only when:

- #30 has defined the applicable data-egress/secret policy for the fixture;
- a staging/qualified LiteLLM path implements the 600-second exact-model target or the probe is explicitly part of `litellm-ckff-ops#24`;
- the installed OpenCode version/config is pinned and the result is recorded under #33.

### General V6 development use

Do not treat the lane as generally qualified for V6 repository work until #33 records that the exact-model, timeout, authority, isolation, data-egress, and independent-verification requirements pass.

## Canonical development inference contract: 600 seconds

For the V6 cross-vendor development lane:

- **one model request ceiling: 600 seconds**;
- OpenCode's provider timeout target is **600000 ms**;
- LiteLLM's model request timeout target is **600 seconds**;
- compatibility bridges must not introduce shorter per-model attempt deadlines;
- lower-timeout backup routes are separate route qualifications, not alternate Cortex inference deadlines;
- an OpenCode/LiteLLM build that terminates a valid request earlier is unqualified for this lane rather than becoming a new Cortex timeout policy.

Streaming is preferred for long generations but does not create a second semantic timeout or extend the 600-second ceiling.

Local tool/subprocess/test/healthcheck timeouts may exist for deterministic operations. They are not model-seat deadlines and must not be scored as model capability failures.

### OpenCode qualification rule

Pin the installed OpenCode version/config, configure the provider request target to `600000` ms, and run a controlled request extending beyond any previously suspected hidden ~300-second cutoff. If the client terminates earlier, reject/upgrade/fix it for this lane.

## Exact model identity; no hidden cross-model fallback

A bootstrap/Cortex seating decision must remain observable end to end.

- Every summon names one exact selected LiteLLM model.
- The V6/OpenCode lane requires cross-model fallback **off by default** below Cortex.
- Transport mechanics may retry only while preserving the same logical selected-model identity.
- A different model/vendor must not be silently substituted.
- If the selected model fails, the attempt returns to the bootstrap/Cortex controller.
- The controller decides whether to retry the same seat or create a separate attempt using another ranked vendor seat.
- Unexpected requested/actual model mismatch invalidates the attempt as seating evidence.

Hidden fallback would corrupt model ranking, vendor diversity, retry counts, cost attribution, and assurance evidence.

## Data-egress authority

Read authority is not automatically egress authority.

Each live external-model packet must be allowed by #30's project/data policy. In particular:

- secrets, credentials, `.env` material, personal data, confidential files, private logs, or unrelated repository contents must not be sent merely because a tool can read them;
- authorized files/tools/effects and authorized external context must be explicit;
- tool output must be treated as model egress too;
- if the packet contains unknown or prohibited data, fail closed and use a local/human path rather than bypassing policy.

## Seating methodology while V6 is built

V5 seating/ranking material is **donor evidence only**. Issue #31 now owns qualification of that donor evidence and of the retry/failure budget before #19.

The following are therefore hypotheses/inputs to qualify, not permanent constants:

- task/risk/role/methodology-derived eligibility;
- strength ranking from current evidence;
- cross-vendor seat diversity;
- a 3-probe failure target;
- a 30-normal-retry ceiling.

A 600-second per-request ceiling makes an unbudgeted retry count dangerous. #31 must define cumulative wall-clock/cost budgets, retryable failure classes, backoff/cooldown, switch/reset semantics, and exact-generation fencing before these values become V6-native policy.

Transport/client/rate-limit/tool/policy failures must not automatically lower model capability ranking.

## Granulation rule

The bootstrap controller/human prepares the granule **before** OpenCode receives it. Do not give a frontier coding agent an unbounded issue such as "implement the whole subsystem."

Each packet should contain:

```text
TASK / WORK UNIT / GENERATION OR REPO REF
ROLE: worker | test-writer | reviewer | researcher | evaluator
OBJECTIVE: one bounded outcome
AUTHORITATIVE INPUTS: exact issue/requirement/current repo refs
FOSSIL CONTEXT: only relevant approved durable facts with provenance
READ AUTHORITY: exact files/repository surfaces that may be inspected
EGRESS AUTHORITY: what information may be sent to the selected external model
MUTATION AUTHORITY: exact workspace/files/effects that may be changed
NON-GOALS: explicit exclusions
ACCEPTANCE: observable check for this granule
REQUIRED EVIDENCE: diff/tests/research/critique to return
MODEL SEAT: exact selected LiteLLM model
REQUEST CEILING: 600 seconds
STOP CONDITION: ambiguity, missing authority, prerequisite failure, unsafe egress, or inability to finish the current model turn inside the request contract
HANDOFF: facts/checkpoint required by the bootstrap controller before any next granule
```

A granule should normally change or answer one thing and have an obvious verification boundary. A larger engineering job proceeds through multiple independently bounded granules; OpenCode returns control between them.

## Role mapping and workspace isolation

- `worker` / `test-writer`: mutating agent in an authorized isolated worktree/workspace.
- `reviewer` / `researcher` / `evaluator`: non-mutating/read-oriented by default.

For independent cross-vendor critique/evaluation, use genuinely independent vendor seats where useful. For multiple mutating workers, each gets an isolated worktree/workspace and explicit non-overlapping or coordinated scope; never point multiple workers at one mutable checkout.

Disable/avoid recursive subagent fan-out and doom-loop recovery for this temporary path. OpenCode may use bounded tools inside one packet, but the bootstrap controller chooses the next packet/model after the packet returns.

## Completion and evidence

Model self-report is never enough.

For mutating packets, return at minimum:

- exact requested/actual model identity and attempt metadata;
- changed files/diff;
- relevant local test/tool results;
- stop/failure reason if incomplete;
- any ambiguity discovered.

Then run the project-owned independent verification/CI/review appropriate to the change. GitHub/CI remains merge authority. A successful OpenCode turn is evidence about an attempted granule, not proof that a V6 requirement is complete.

## Seating donor evidence

Historical V5 model rankings may be consulted as priors only. They must be intersected with the live provider/model catalog, current health, task suitability, privacy/egress eligibility, vendor independence, and newer measured evidence.

Do not hard-code a historical frontier list into V6 truth. #31/#19 own the later qualification and native seating policy.

## What is deliberately not implemented yet

This runbook does **not** add a V6 LiteLLM client, model router, OpenCode dispatcher module, runtime adapter, lifecycle integration, or automatic recursive agent organization.

When #19's corrected entry gates are eventually satisfied, derive the native transport/seating contract from qualified V6 needs and evidence. Do not copy the retired V5 runtime or make the bootstrap shell permanent by accident.

## Resume rule

Before cross-vendor frontier-agent work, read in order:

1. `docs/V6_FRESH_SESSION_AUDIT_2026-08-18.md` / issue #25;
2. this runbook;
3. #30 (egress), #31 (seating/retry qualification), and #33 (OpenCode bootstrap qualification);
4. `Pukujan/litellm-ckff-ops` main README + `docs/TIMEOUT-CONTRACT.md` + issue #24;
5. the current project issue/accepted SHA governing the actual granule.

If those sources conflict with older implementation-specific handoff text, the fresh audit/supersession chain wins unless #25 records a later disposition.