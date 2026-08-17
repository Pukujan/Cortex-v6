# Cortex V6 Governance

## Why this exists

Cortex is a long-running architecture project. Untracked implementation, undocumented boundary changes, and code that silently bypasses intended components were major historical failure modes. V6 therefore makes traceability part of the development process, while keeping the process deliberately small.

## Bootstrap exception

Issue #1 is the one-time bootstrap authorization for creating the initial repository governance and documentation directly on `main`. The repository was empty, so no PR gate could exist before this bootstrap.

After #1, normal substantive changes should use a pull request and satisfy the rules below.

## Required change record

Every non-trivial PR must have:

1. **A tracking issue** — the PR body contains `Tracking: #<issue>`.
2. **A narrow problem statement** — the issue explains what is wrong or missing, not only what code to add.
3. **Acceptance criteria** — a mechanical or observable condition for completion.
4. **Documentation impact** — either durable docs are changed in the PR, or the PR explicitly records why no durable documentation is affected.
5. **Evidence** — tests/checks appropriate to the change.

The docs gate checks items 1 and 4 mechanically. Other gates are added only when the underlying capability exists.

## Documentation rule

A substantive implementation/configuration change must do one of the following:

- change `README.md` or a file under `docs/`; or
- include a PR body line of the form:

  `Docs-Impact: none - <specific reason>`

A blank or generic reason such as `none`, `n/a`, or `no` is not sufficient.

This rule is intentionally about **traceability**, not documentation volume. Small bug fixes should not be forced to churn architecture docs when the durable system model did not change.

## Architecture growth rule

A proposed new Cortex mechanism must answer in its issue:

- What exact problem exists now?
- What is the simplest baseline without the mechanism?
- Does mature software already solve the problem?
- What new failure modes would the mechanism create?
- What measurable acceptance test shows that it pays for its complexity?

Difficulty alone does not justify a new product/module boundary.

## Ownership and state

Until a stronger need is proven, prefer one authoritative writer for authoritative state rather than inventing broad semantic-ownership frameworks.

At minimum:

- task/requirement state is not mutated by arbitrary components;
- FOSSIL owns durable knowledge state, not Cortex operational workflow state;
- model/worker output cannot directly mark a task complete;
- verification evidence must be produced by the declared verification path.

## Pull request expectations

PRs should remain small enough that a reviewer can answer:

- Which tracked problem does this solve?
- Which invariant or behavior changes?
- Which files/components are now authoritative for that behavior?
- What proves the real composed path works?

A PR that cannot answer those questions should be split or returned to research.

## Required GitHub enforcement

The workflow `.github/workflows/docs-gate.yml` must be configured as a **required status check** on `main`; otherwise it is advisory only. Repository branch/ruleset configuration is tracked in #8.

Once #2 lands, the ordinary SWE checks (lint/type/test/etc.) should also be required.

## Emergency bypass

If an owner must bypass normal process for an emergency, the bypass must be explicit and followed by a tracking issue describing:

- why the normal gate could not be used;
- what changed;
- what evidence was obtained afterward;
- what prevents the bypass from becoming the normal path.

Hidden or undocumented bypasses are not acceptable architecture.
