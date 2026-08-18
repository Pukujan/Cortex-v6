"""Stable task-state and bounded-context invariants recovered from Cortex V4."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field, replace


class ContextBudgetError(ValueError):
    """Raised when the context cannot fit without dropping protected semantics."""


class ContextPreservationError(RuntimeError):
    """Raised when a protected semantic span is absent from rendered context."""


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(text for value in (values or ()) if (text := str(value).strip()))


@dataclass(frozen=True)
class StableTaskState:
    """Semantic task state that is never inferred from or compacted with transcript text."""

    goals: tuple[str, ...]
    constraints: tuple[str, ...] = ()
    accepted_decisions: tuple[str, ...] = ()
    unresolved_questions: tuple[str, ...] = ()
    completion_criteria: tuple[str, ...] = ()

    @classmethod
    def create(
        cls,
        *,
        goals: Iterable[str],
        constraints: Iterable[str] | None = None,
        accepted_decisions: Iterable[str] | None = None,
        unresolved_questions: Iterable[str] | None = None,
        completion_criteria: Iterable[str] | None = None,
    ) -> StableTaskState:
        clean_goals = _clean(goals)
        if not clean_goals:
            raise ValueError("stable task state requires at least one goal")
        return cls(
            goals=clean_goals,
            constraints=_clean(constraints),
            accepted_decisions=_clean(accepted_decisions),
            unresolved_questions=_clean(unresolved_questions),
            completion_criteria=_clean(completion_criteria),
        )

    def updated(
        self,
        *,
        goals: Iterable[str] | None = None,
        add_goals: Iterable[str] | None = None,
        constraints: Iterable[str] | None = None,
        accepted_decisions: Iterable[str] | None = None,
        unresolved_questions: Iterable[str] | None = None,
        completion_criteria: Iterable[str] | None = None,
    ) -> StableTaskState:
        if goals is not None:
            next_goals = _clean(goals)
            if not next_goals:
                raise ValueError("required field 'goals' must not be emptied")
        else:
            next_goals = self.goals
            if add_goals is not None:
                next_goals = tuple(dict.fromkeys((*next_goals, *_clean(add_goals))))

        def pick(current: tuple[str, ...], values: Iterable[str] | None) -> tuple[str, ...]:
            return current if values is None else _clean(values)

        return replace(
            self,
            goals=next_goals,
            constraints=pick(self.constraints, constraints),
            accepted_decisions=pick(self.accepted_decisions, accepted_decisions),
            unresolved_questions=pick(self.unresolved_questions, unresolved_questions),
            completion_criteria=pick(self.completion_criteria, completion_criteria),
        )


def render_stable(state: StableTaskState) -> str:
    """Render all stable semantics deterministically for context-preservation checks."""

    lines = ["## Stable task state (never compacted)"]
    sections = (
        ("Goals", state.goals),
        ("Constraints", state.constraints),
        ("Accepted decisions", state.accepted_decisions),
        ("Unresolved questions", state.unresolved_questions),
        ("Completion criteria", state.completion_criteria),
    )
    for title, items in sections:
        if not items:
            continue
        lines.append(f"### {title}")
        lines.extend(f"- {item}" for item in items)
    return "\n".join(lines)


@dataclass(frozen=True)
class OffloadPointer:
    """Pointer replacing expendable context while retaining the offloaded payload locally."""

    key: str

    def __str__(self) -> str:
        return f"offload:{self.key}"


@dataclass(frozen=True)
class OffloadRecord:
    pointer: OffloadPointer
    body: str


@dataclass(frozen=True)
class ContextItem:
    body: str
    protected: bool = False
    pointer: OffloadPointer | None = None


@dataclass
class ContextController:
    """Bound working context that offloads expendable text and fails closed on loss."""

    max_chars: int
    task_state: StableTaskState
    _items: list[ContextItem] = field(default_factory=list)
    _offloaded: list[OffloadRecord] = field(default_factory=list)
    _sequence: int = 0

    def __post_init__(self) -> None:
        if self.max_chars < 1:
            raise ValueError("max_chars must be positive")

    def add_text(self, text: str, *, protected: bool = False) -> None:
        self._items.append(ContextItem(body=text, protected=protected))

    def protected_spans(self) -> tuple[str, ...]:
        return (
            render_stable(self.task_state),
            *(item.body for item in self._items if item.protected and item.body),
        )

    def render(self) -> str:
        return "\n\n".join((render_stable(self.task_state), *(item.body for item in self._items)))

    def validate_preservation(self, rendered: str | None = None) -> None:
        material = self.render() if rendered is None else rendered
        missing = tuple(span for span in self.protected_spans() if span and span not in material)
        if missing:
            raise ContextPreservationError(f"context dropped {len(missing)} protected span(s)")

    def compact(self) -> tuple[OffloadRecord, ...]:
        while len(self.render()) > self.max_chars:
            index = next(
                (
                    i
                    for i, item in enumerate(self._items)
                    if not item.protected and item.pointer is None
                ),
                None,
            )
            if index is None:
                self.validate_preservation()
                raise ContextBudgetError("context cannot fit without dropping protected semantics")

            item = self._items[index]
            self._sequence += 1
            pointer = OffloadPointer(f"O{self._sequence:04d}")
            record = OffloadRecord(pointer=pointer, body=item.body)
            self._offloaded.append(record)
            self._items[index] = ContextItem(body=str(pointer), pointer=pointer)

        self.validate_preservation()
        return tuple(self._offloaded)

    def offloaded(self) -> tuple[OffloadRecord, ...]:
        return tuple(self._offloaded)
