from dataclasses import replace
from pathlib import Path, PurePosixPath

import pytest

from cortex_v6.walking import (
    AuthorityError,
    RequirementState,
    admit_completion,
    apply_filesystem_effect,
    make_work_unit,
    run_exact_text_task,
)


def requirement(*, target: str = "result.txt", version: int = 1) -> RequirementState:
    return RequirementState(
        requirement_id="R-1",
        version=version,
        target=PurePosixPath(target),
        expected_text="required output\n",
    )


def test_walking_skeleton_positive_case_uses_production_path(tmp_path: Path) -> None:
    req = requirement()

    result = run_exact_text_task(
        req,
        authority_root=tmp_path,
        generation=1,
        candidate_text="required output\n",
        transcript="noise-" * 500,
        context_budget_chars=256,
    )

    assert result.completed is True
    assert (tmp_path / "result.txt").read_text(encoding="utf-8") == req.expected_text
    assert result.context.size_chars <= result.context.budget_chars
    assert f"requirement_id={req.requirement_id}" in result.context.protected
    assert f"expected_text={req.expected_text}" in result.context.protected


def test_out_of_authority_effect_is_refused(tmp_path: Path) -> None:
    req = requirement()
    work = replace(
        make_work_unit(req, generation=1, authority_root=tmp_path),
        target=PurePosixPath("../escape.txt"),
    )

    with pytest.raises(AuthorityError):
        apply_filesystem_effect(work, "required output\n")

    assert not (tmp_path.parent / "escape.txt").exists()


def test_incorrect_output_cannot_complete(tmp_path: Path) -> None:
    result = run_exact_text_task(
        requirement(),
        authority_root=tmp_path,
        generation=1,
        candidate_text="worker claims success but writes the wrong bytes\n",
    )

    assert result.receipt.verified is False
    assert result.completed is False


def test_stale_generation_receipt_cannot_complete(tmp_path: Path) -> None:
    req = requirement()
    old = run_exact_text_task(
        req,
        authority_root=tmp_path,
        generation=1,
        candidate_text=req.expected_text,
    )
    current_work = make_work_unit(req, generation=2, authority_root=tmp_path)

    assert old.receipt.verified is True
    assert admit_completion(req, current_work, old.receipt) is False


def test_mismatched_requirement_version_receipt_cannot_complete(tmp_path: Path) -> None:
    old_requirement = requirement(version=1)
    old = run_exact_text_task(
        old_requirement,
        authority_root=tmp_path,
        generation=1,
        candidate_text=old_requirement.expected_text,
    )
    current_requirement = requirement(version=2)
    current_work = make_work_unit(current_requirement, generation=1, authority_root=tmp_path)

    assert admit_completion(current_requirement, current_work, old.receipt) is False
