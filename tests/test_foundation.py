from hypothesis import given, strategies as st

import cortex_v6


def test_package_imports() -> None:
    assert cortex_v6.__all__ == ()


@given(st.text())
def test_trivial_hypothesis_property_preserves_text(value: str) -> None:
    assert value.encode().decode() == value
