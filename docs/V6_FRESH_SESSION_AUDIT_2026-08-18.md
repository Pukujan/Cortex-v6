# V6 Fresh-Session Plan Audit — 2026-08-18

**Status:** authoritative audit addendum for planning; tracked by #25.  
**Evidence pack:** `Pukujan/fossil-cortex-v6@29ceac9`.  
**Scope:** re-check the long-session V6 roadmap before implementation expands beyond the minimal kernel floor.

This document does not discard the useful parts of `V6_LOCKED_PLAN.md`. It records which decisions survived a fresh-session audit and which must be downgraded from "locked" implementation direction to hypotheses requiring qualification.

## Executive verdict

The long session did **not** produce a uniformly bad plan. The first implementation floor is notably disciplined:

```text
#2 ordinary SWE foundation
  -> #3 one real walking skeleton
  -> #4 V4 stable-state/context invariants
     + #7 SCC-v2 adversarial composition regressions
```

PRs #21-#24 remain narrow and deliberately avoid provider/runtime expansion. The FOSSIL lineage pack also handles the reconstructed shared-chat checkpoint correctly: it is low-authority reconstructed evidence, while Issue #9, the locked plan, and PR snapshots are primary.

The main context-rot risk appears **after** the kernel floor: the roadmap converts several plausible hypotheses into a "locked" future architecture before the experiments needed to justify them have run.

## Decisions that remain stable

These are architecture invariants or ownership principles that do not depend on a vendor/framework winner:

1. **Project owns current project truth.** Current requirements/source/tests/config/acceptance meaning outrank stale historical memory.
2. **V6 owns authoritative control semantics.** Stable requirement/work/generation identity, authority, evidence admission, and lifecycle transitions cannot be delegated accidentally to a model/runtime/provider.
3. **Transcript/model assertions are not authoritative task state or completion evidence.**
4. **External systems return results/evidence; they do not directly mark V6 work complete.**
5. **V5/SCC v1/v2 are donors/oracles/failure corpora, not runtime inheritance trees.**
6. **FOSSIL owns durable knowledge/provenance/lineage, not active V6 lifecycle state.**
7. **GitHub/CI remains an independent repository merge authority.**
8. **The kernel must be qualified externally before autonomous V6 assurance routing is trusted.**
9. **Added mechanism must beat a serious simpler baseline or be narrowed/removed.**
10. **The temporary development path uses pre-granulated work and exact model seats rather than recursively widening one frontier-agent prompt.**

## Decisions downgraded to hypotheses

### Microsoft Agent Framework first

Still a plausible candidate, not a permanent architecture fact. Current official Microsoft material describes Agent Framework as an open Python/.NET agent and orchestration framework. It should be qualified against the direct/local baseline after the integrated kernel reveals the actual framework needs.

`no framework abstraction needed yet` must be a valid experimental result.

### AWS AgentCore as the portability challenger

The earlier plan treated AgentCore as a peer replacement for the Microsoft "runtime." Fresh vendor validation shows a layer mismatch: AgentCore Runtime is framework-agnostic managed hosting/runtime infrastructure. AWS explicitly supports bringing custom agent code or another framework and retaining the orchestration loop.

Therefore framework portability and hosting/runtime portability must be separated. AgentCore may host a Microsoft-Agent-Framework-based V6 application rather than replace that framework.

Tracked by #27.

### Generic `AgentRuntime` port

Do not create one because the roadmap names it. First inventory what the accepted walking path actually needs. The experiment may conclude that direct/local execution remains simpler until a second real execution substrate creates pressure for a seam.

### `AssurancePlan` / provider / receipt abstraction

The exact evidence-binding principle remains strong. The generalized provider boundary must still earn itself against direct CI invocation of two genuinely heterogeneous assurance methods. Avoid creating a methodology/plugin framework.

### Fixed agent role vocabulary/topologies

Worker/reviewer/assurance authority separation is useful. Exact role names and multi-agent topology should be derived from demonstrated work modes, not treated as a product ontology. Ordinary bounded work must remain single-path when fanout adds no measured value.

### FOSSIL context composition

No winner is selected. Live project is current-fact authority. Project-only, FOSSIL-only, and hybrid remain #17 experiment conditions; results should be segmented by task class. FOSSIL-only is a control/possible special-case path, not a substitute for current project truth.

### 3-probe / 30-normal model retry policy

Keep as a V6 target hypothesis, not inherited truth. #31 requires V5 donor qualification, failure taxonomy, cumulative wall-clock/cost budgets, and fake-catalog/fault testing before #19 implementation. Transport/rate-limit/tool/policy failures must not be mis-scored as model incapability.

## Material roadmap corrections

### 1. Prove the combined kernel, not sibling-green components

PRs #23 and #24 are siblings and both modify `src/cortex_v6/walking.py`. Their current hunks appear compatible but their **combined composition is not yet the CI-qualified subject**.

#26 requires one exact SHA containing both accepted behaviors and a full production-path suite before later architecture starts.

### 2. Move value gates earlier

#18's final system benchmark is good but too late as the first serious value test. #28 adds progressive A/B kill gates after the kernel and before each major abstraction so sunk cost does not become the justification for continuing.

### 3. Split bootstrap qualification from assurance orchestration

#15 currently depends on #14 despite saying V6 must be independently qualified. #29 splits this:

- Phase A: ordinary CI externally attacks the integrated kernel immediately after the #4/#7 floor;
- Phase B: after #14, independently qualify V6's assurance-orchestration behavior itself.

### 4. Add data-egress authority before live external models

The CKFF gateway contract states it is not verified zero-data-retention and prohibits sending secrets/personal/confidential data. Model-seat eligibility therefore needs a data-egress dimension independent of read/write mutation authority.

#30 gates live OpenCode/LiteLLM use on classification, secret/egress controls, and provider-route privacy qualification.

### 5. Decouple legacy runtime retirement from FOSSIL selection

Basic proof that V6 no longer needs SSC v1 should happen as soon as #4 is integrated. It should not wait for #17's later context-source bakeoff. #32 separates those concerns.

## Corrected temporary cross-vendor development contract

`docs/CROSS_VENDOR_DEV_EXECUTION.md` is the operational source. The key rules are:

- one model request ceiling: **600 seconds**;
- OpenCode provider timeout target: **600000 ms**;
- exact selected model identity end to end;
- hidden cross-model fallback below Cortex is off by default;
- Cortex/bootstrap policy owns retry and cross-vendor switching;
- V5 seating is donor evidence only;
- pre-granulate every work packet before OpenCode receives it;
- no live external-model packet until #30's data-egress gate and the LiteLLM transport qualification are satisfied.

The remaining LiteLLM implementation mismatch is tracked in `Pukujan/litellm-ckff-ops#24`.

## Audit issue tree

- #25 — fresh-session audit/re-baseline parent.
- #26 — combined #4/#7 production composition qualification.
- #27 — separate framework portability from hosting/runtime portability.
- #28 — progressive value/kill gates.
- #29 — independent kernel qualification before V6 assurance orchestration.
- #30 — data-egress/secret policy for live OpenCode/LiteLLM development.
- #31 — V5 seating donor + retry/failure/budget qualification before #19.
- #32 — early SSC retirement separate from #17 context bakeoff.

## Corrected near-term order

Do **not** start by implementing #10.

```text
1. Review/accept #21 (#2)
2. Rebase/review/accept #22 (#3)
3. Integrate #23 + #24 and prove the combined kernel (#26)
4. Run bootstrap external kernel qualification (#29 Phase A)
5. Run the first minimal-kernel value gate (#28 Gate A)
6. Prove SSC v1 is absent from the live kernel path (#32 early phase)
7. Resolve #27 before redefining #10-#12
8. Qualify data-egress + LiteLLM/OpenCode transport before live cross-vendor development (#30 + litellm-ckff-ops#24)
9. Qualify any V5 donors actually needed (#5 / #31)
10. Only then expand later mechanisms one at a time behind their progressive gates
```

## Resume rule

A future agent should read, in order:

1. this audit addendum;
2. #25 and unresolved child issues;
3. `V6_LOCKED_PLAN.md` for the original rationale/invariants;
4. current accepted kernel SHA/PR state;
5. `CROSS_VENDOR_DEV_EXECUTION.md` before any external frontier-agent work.

If this audit conflicts with an older implementation-specific "locked" choice, treat the older choice as under revalidation unless #25 records a resolved disposition restoring it.