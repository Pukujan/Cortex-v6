"""The single V6 walking-skeleton path tracked by issue #3.

This module deliberately proves only one task shape: write exact required text inside a bounded
filesystem authority and admit completion only after an independent read-back verifier succeeds.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath


class ContextBudgetError(ValueError):
    """Raised when protected requirement state cannot fit in the context budget."""


class AuthorityError(PermissionError):
    """Raised when a work unit attempts an effect outside its declared authority."""


@dataclass(frozen=True)
class RequirementState:
    """Stable semantic task state, independent of transcript/message history."""

    requirement_id: str
    version: int
    target: PurePosixPath
    expected_text: str

    def __post_init__(self) -> None:
        if not self.requirement_id:
            raise ValueError("requirement_id must be non-empty")
        if self.version < 1:
            raise ValueError("version must be positive")


@dataclass(frozen=True)
class BoundedContext:
    """Protected requirement state plus expendable transcript under one hard budget."""

    protected: str
    expendable: str
    budget_chars: int

    @property
    def size_chars(self) -> int:
        return len(self.protected) + len(self.expendable)


@dataclass(frozen=True)
class WorkUnit:
    """One exact execution attempt with bounded filesystem authority."""

    work_unit_id: str
    generation: int
    requirement_id: str
    requirement_version: int
    authority_root: Path
    target: PurePosixPath


@dataclass(frozen=True)
class VerificationReceipt:
    """Independent verification evidence bound to one exact work generation."""

    requirement_id: str
    requirement_version: int
    work_unit_id: str
    generation: int
    target: PurePosixPath
    observed_sha256: str
    verified: bool


@dataclass(frozen=True)
class TaskResult:
    """Result admitted by the kernel after evidence validation."""

    work_unit: WorkUnit
    context: BoundedContext
    receipt: VerificationReceipt
    completed: bool


def compose_context(
    requirement: RequirementState,
    transcript: str,
    *,
    budget_chars: int,
) -> BoundedContext:
    """Build bounded context while refusing to compact protected requirement semantics."""

    if budget_chars < 1:
        raise ContextBudgetError("context budget must be positive")

    protected = (
        f"requirement_id={requirement.requirement_id}\n"
        f"version={requirement.version}\n"
        f"target={requirement.target.as_posix()}\n"
        f"expected_text={requirement.expected_text}"
    )
    if len(protected) > budget_chars:
        raise ContextBudgetError("protected requirement state exceeds context budget")

    remaining = budget_chars - len(protected)
    expendable = transcript[-remaining:] if remaining else ""
    context = BoundedContext(protected=protected, expendable=expendable, budget_chars=budget_chars)
    if context.size_chars > budget_chars:
        raise AssertionError("bounded context exceeded its declared budget")
    return context


def make_work_unit(
    requirement: RequirementState,
    *,
    generation: int,
    authority_root: Path,
) -> WorkUnit:
    """Bind one work unit to the exact requirement version and execution generation."""

    if generation < 1:
        raise ValueError("generation must be positive")
    return WorkUnit(
        work_unit_id=f"{requirement.requirement_id}:v{requirement.version}:g{generation}",
        generation=generation,
        requirement_id=requirement.requirement_id,
        requirement_version=requirement.version,
        authority_root=authority_root,
        target=requirement.target,
    )


def apply_filesystem_effect(work: WorkUnit, candidate_text: str) -> Path:
    """Apply the one allowed effect, refusing absolute, traversal, and symlink escapes."""

    if work.target.is_absolute() or ".." in work.target.parts or not work.target.parts:
        raise AuthorityError("target is outside declared relative authority")

    root = work.authority_root.resolve(strict=False)
    target = root.joinpath(*work.target.parts)
    parent = target.parent.resolve(strict=False)
    if not parent.is_relative_to(root):
        raise AuthorityError("target parent escapes authority root")
    if target.is_symlink():
        raise AuthorityError("symlink target is not an admissible effect")

    parent.mkdir(parents=True, exist_ok=True)
    target.write_text(candidate_text, encoding="utf-8")
    return target


def verify_exact_output(
    requirement: RequirementState,
    work: WorkUnit,
    target: Path,
) -> VerificationReceipt:
    """Read back the real effect and produce evidence; never trust the candidate assertion."""

    observed = target.read_text(encoding="utf-8")
    digest = sha256(observed.encode("utf-8")).hexdigest()
    return VerificationReceipt(
        requirement_id=requirement.requirement_id,
        requirement_version=requirement.version,
        work_unit_id=work.work_unit_id,
        generation=work.generation,
        target=work.target,
        observed_sha256=digest,
        verified=observed == requirement.expected_text,
    )


def admit_completion(
    requirement: RequirementState,
    work: WorkUnit,
    receipt: VerificationReceipt,
) -> bool:
    """Fail closed unless PASS evidence is bound to the exact current inputs and generation."""

    expected_digest = sha256(requirement.expected_text.encode("utf-8")).hexdigest()
    return (
        receipt.verified
        and receipt.observed_sha256 == expected_digest
        and receipt.requirement_id == requirement.requirement_id
        and receipt.requirement_version == requirement.version
        and receipt.work_unit_id == work.work_unit_id
        and receipt.generation == work.generation
        and receipt.target == work.target
        and work.requirement_id == requirement.requirement_id
        and work.requirement_version == requirement.version
    )


def run_exact_text_task(
    requirement: RequirementState,
    *,
    authority_root: Path,
    generation: int,
    candidate_text: str,
    transcript: str = "",
    context_budget_chars: int = 1_024,
) -> TaskResult:
    """Traverse the sole production composition path for the issue #3 walking skeleton."""

    context = compose_context(requirement, transcript, budget_chars=context_budget_chars)
    work = make_work_unit(requirement, generation=generation, authority_root=authority_root)
    target = apply_filesystem_effect(work, candidate_text)
    receipt = verify_exact_output(requirement, work, target)
    return TaskResult(
        work_unit=work,
        context=context,
        receipt=receipt,
        completed=admit_completion(requirement, work, receipt),
    )
