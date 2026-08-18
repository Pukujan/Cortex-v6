# Cross-vendor development execution while V6 is under construction

**Status:** operational development runbook only. This does not implement #19 and does not change the locked #2 -> #3 -> #4/#7 integration order.

## Purpose

Cortex V5 is retired. V5 may be consulted only as a historical donor/reference for methodology names, measured model-tier evidence, or failure lessons. No live V6 execution path should depend on the V5 runtime.

Until V6 has earned and implemented its own model/runtime boundary, cross-vendor coding, test-writing, review, and research that require a repository-aware frontier agent should use OpenCode as an external execution shell over the LiteLLM-compatible ckff endpoint.

The temporary development flow is:

```text
live Cortex-v6 repository + FOSSIL durable context
                    |
                    v
V6/current methodology + task/risk requirements
                    |
                    v
cross-vendor seat selection using qualified live catalog evidence
                    |
                    v
pre-granulated task packet
                    |
                    v
OpenCode CLI -> explicit ckff model seat
                    |
                    v
workspace change / tests / research / critique
                    |
                    v
project tests + independent assurance + GitHub/CI
```

OpenCode is not authoritative Cortex state. LiteLLM/ckff is transport. FOSSIL is not active task state. Project tests and later V6 evidence admission remain the completion authority.

## Ownership split

- **Live project:** current requirements, source, tests, config, ADRs, acceptance meaning, Git state.
- **FOSSIL:** durable research, provenance, lineage, historical failures, prior evidence and reusable knowledge. Current live repository state wins conflicts about present project facts.
- **Cortex/V6 policy:** task/risk classification, role/topology choice, model-seat eligibility, evidence requirements, and later lifecycle transitions.
- **OpenCode:** temporary repository-aware coding/research/reviewer execution shell.
- **LiteLLM/ckff:** model transport only.
- **Project assurance/GitHub:** deterministic checks, review, CI and merge authority.

## ckff route envelopes

Operator-visible ckff dashboard text supplied on 2026-08-18 records:

| Endpoint | Node | Network timeout | Operational rule |
|---|---|---:|---|
| `https://ckffai.com/v1` | Tencent / recommended | 600 s | prefer for stability and long streamed calls |
| `https://aws.ckffai.com/v1` | AWS / backup | 180 s | non-stream requests over 180 s may fail; prefer streaming or the primary route |

These are route/execution-envelope facts, not model-quality facts. If several models on the same route fail at the same ceiling, do not score that as independent model incapability.

### Timeout classes must stay distinct

Do not collapse these into one `timeout`:

- provider/route request ceiling;
- OpenCode provider-request timeout;
- stream/chunk inactivity timeout;
- client read timeout;
- local tool/subprocess timeout;
- verification/test timeout.

When #19 is eventually implemented, these must remain separately observable and must not silently become model-seating failure evidence.

## Streaming and OpenCode request budget

Always use streaming for long model work. Streaming can prevent idle-connection failures but cannot defeat an absolute provider/request ceiling.

Current OpenCode documentation exposes provider request timeout settings, including `provider.*.options.timeout` and a separate chunk timeout. Configure the ckff provider for the 600 s primary route, but qualify the installed OpenCode version before relying on turns longer than 300 s because upstream versions have been reported to terminate near that boundary despite larger configuration.

Until local qualification proves otherwise:

- primary 600 s route: target individual model turns <= 240 s;
- backup 180 s route: target individual model turns roughly 60-120 s;
- a longer coding job may continue across multiple bounded model turns and tool operations inside one foreground OpenCode session;
- never replay one oversized packet against vendor after vendor merely because the previous seat timed out on the same route.

## Granulation rule

The controller/human prepares the granule **before** OpenCode receives it. Do not give a frontier coding agent an unbounded issue such as “implement the whole subsystem.”

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
TIME BUDGET: route-aware turn budget
STOP CONDITION: ambiguity, missing authority, prerequisite failure, or budget risk
HANDOFF: facts/checkpoint required by the next granule
```

A granule should normally change or answer one thing and have an obvious verification boundary.

## Role mapping

Use OpenCode as an execution shell, not an autonomous recursive organization.

- `worker` / `test-writer`: mutating coding agent in an authorized isolated workspace.
- `reviewer` / `researcher` / `evaluator`: non-mutating/read-oriented agent; allow web/repository research as needed but do not grant write authority by convenience.

For independent cross-vendor critique or evaluation, use seats from different vendors. For multiple mutating workers, give each seat an isolated worktree/workspace; never point multiple workers at one mutable checkout.

Disable or avoid recursive subagent fan-out and doom-loop style recovery for this path. Cortex/human granulation chooses the next bounded packet rather than allowing an execution agent to recursively widen the task.

## Seating donor evidence

V5's measured seating research may be reused as **donor evidence only**, not as V6 runtime code or permanent truth. Its last recorded five-vendor frontier prior was:

1. `grok-4.6` — xAI
2. `gpt-5.6-sol` — OpenAI
3. `kimi-k3` — Moonshot
4. `qwen3.8-max` — Alibaba
5. `gemini-3.6-flash` — Google

Before each consequential cross-vendor run, intersect any prior with the live LiteLLM/ckff catalog, route health, task suitability, and newer measured evidence. #19 still owns the eventual V6-native seating contract and must qualify it independently.

## What is deliberately not implemented yet

This runbook does **not** add a V6 LiteLLM client, model router, OpenCode dispatcher module, runtime adapter, or lifecycle integration. Doing that now would bypass the locked dependency gates.

When #19's entry gates are satisfied, its implementation should derive the V6 transport contract from current V6 needs and this operational evidence. It must not copy the retired V5 runtime wholesale.

## Resume rule

Any agent resuming Cortex V6 should read this file together with `docs/V6_LOCKED_PLAN.md` and issue #19 before doing cross-vendor frontier-agent work. Treat V5 as frozen historical evidence only.