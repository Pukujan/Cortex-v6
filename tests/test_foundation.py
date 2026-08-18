import hypothesis


def test_package_imports() -> None:
    import cortex_v6

    assert cortex_v6.__all__ == ()


@hypothesis.given(hypothesis.strategies.text())
def test_trivial_hypothesis_property_preserves_text(value: str) -> None:
    assert value.encode().decode() == value
