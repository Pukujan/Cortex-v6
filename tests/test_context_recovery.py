import json
from pathlib import Path
from typing import TypedDict, cast

import hypothesis
import pytest

from cortex_v6.context import (
    ContextBudgetError,
    ContextController,
    ContextPreservationError,
    StableTaskState,
    render_stable,
)


class V4Fixture(TypedDict):
    source_repository: str
    source_commit: str
    source_files: list[str]
    goal_marker: str
    protected_text: str
    requires_offload_under_pressure: bool
    rejects_empty_goals: bool


def load_v4_fixture() -> V4Fixture:
    path = Path(__file__).parent / "fixtures" / "v4_context_contract.json"
    return cast(V4Fixture, json.loads(path.read_text(encoding="utf-8")))


def test_v4_cross_runtime_behavior_fixture() -> None:
    fixture = load_v4_fixture()
    state = StableTaskState.create(goals=[fixture["goal_marker"]])
    controller = ContextController(max_chars=400, task_state=state)
    controller.add_text(fixture["protected_text"], protected=True)
    for index in range(12):
        controller.add_text(("noise " * 30) + str(index))

    offloaded = controller.compact()

    assert fixture["source_repository"] == "Pukujan/cortex-v4"
    assert len(fixture["source_commit"]) == 40
    assert fixture["goal_marker"] in controller.render()
    assert fixture["protected_text"] in controller.render()
    assert bool(offloaded) is fixture["requires_offload_under_pressure"]


def test_stable_goals_cannot_silently_disappear() -> None:
    state = StableTaskState.create(goals=["ship correct behavior"], constraints=["no bypass"])
    updated = state.updated(add_goals=["retain original goal"])

    assert updated.goals == ("ship correct behavior", "retain original goal")
    with pytest.raises(ValueError):
        state.updated(goals=[])


def test_context_fails_closed_when_protected_state_cannot_fit() -> None:
    state = StableTaskState.create(goals=["G" * 200])
    controller = ContextController(max_chars=40, task_state=state)

    with pytest.raises(ContextBudgetError):
        controller.compact()


def test_deliberate_protected_field_drop_mutant_is_killed() -> None:
    state = StableTaskState.create(
        goals=["critical-goal"],
        completion_criteria=["critical-criterion"],
    )
    controller = ContextController(max_chars=500, task_state=state)
    rendered = controller.render()
    mutant = rendered.replace("critical-criterion", "")

    with pytest.raises(ContextPreservationError):
        controller.validate_preservation(mutant)


@hypothesis.given(
    hypothesis.strategies.lists(
        hypothesis.strategies.text(
            alphabet=hypothesis.strategies.characters(min_codepoint=32, max_codepoint=126),
            min_size=1,
            max_size=12,
        ),
        min_size=1,
        max_size=10,
    )
)
def test_protected_state_survives_generated_context_pressure(noise: list[str]) -> None:
    state = StableTaskState.create(goals=["protected-goal"], constraints=["protected-constraint"])
    controller = ContextController(max_chars=500, task_state=state)
    controller.add_text("protected-span", protected=True)
    for text in noise:
        controller.add_text(text * 30)

    controller.compact()
    rendered = controller.render()

    assert len(rendered) <= controller.max_chars
    assert render_stable(state) in rendered
    assert "protected-span" in rendered
