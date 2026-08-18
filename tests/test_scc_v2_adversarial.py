from pathlib import Path, PurePosixPath

import pytest

import cortex_v6.walking as walking


class WiringSentinel(RuntimeError):
    """Raised by an intentionally bad seam replacement in composition tests."""


def _requirement(*, target: str = "result.txt") -> walking.RequirementState:
    return walking.RequirementState(
        requirement_id="R-SCC-7",
        version=3,
        target=PurePosixPath(target),
        expected_text="exact effect\n",
    )


def test_scc_v2_regression_production_path_cannot_bypass_authority_gate(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    def refusing_effect(work: walking.WorkUnit, candidate_text: str) -> Path:
        del work, candidate_text
        raise WiringSentinel("authority gate invoked")

    monkeypatch.setattr(walking, "apply_filesystem_effect", refusing_effect)

    with pytest.raises(WiringSentinel, match="authority gate invoked"):
        walking.run_exact_text_task(
            _requirement(),
            authority_root=tmp_path,
            generation=1,
            candidate_text="exact effect\n",
        )


def test_scc_v2_regression_production_path_cannot_bypass_verifier(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    def refusing_verifier(
        requirement: walking.RequirementState,
        work: walking.WorkUnit,
        target: Path,
    ) -> walking.VerificationReceipt:
        del requirement, work, target
        raise WiringSentinel("verifier invoked")

    monkeypatch.setattr(walking, "verify_exact_output", refusing_verifier)

    with pytest.raises(WiringSentinel, match="verifier invoked"):
        walking.run_exact_text_task(
            _requirement(),
            authority_root=tmp_path,
            generation=1,
            candidate_text="exact effect\n",
        )


def test_scc_v2_regression_forged_pass_with_wrong_effect_hash_is_rejected(
    tmp_path: Path,
) -> None:
    requirement = _requirement()
    work = walking.make_work_unit(requirement, generation=4, authority_root=tmp_path)
    forged = walking.VerificationReceipt(
        requirement_id=requirement.requirement_id,
        requirement_version=requirement.version,
        work_unit_id=work.work_unit_id,
        generation=work.generation,
        target=work.target,
        observed_sha256="0" * 64,
        verified=True,
    )

    assert walking.admit_completion(requirement, work, forged) is False


def test_scc_v2_regression_stale_generation_pass_is_rejected(tmp_path: Path) -> None:
    requirement = _requirement()
    old_work = walking.make_work_unit(requirement, generation=1, authority_root=tmp_path)
    old_path = walking.apply_filesystem_effect(old_work, requirement.expected_text)
    old_receipt = walking.verify_exact_output(requirement, old_work, old_path)
    current_work = walking.make_work_unit(requirement, generation=2, authority_root=tmp_path)

    assert old_receipt.verified is True
    assert walking.admit_completion(requirement, current_work, old_receipt) is False
