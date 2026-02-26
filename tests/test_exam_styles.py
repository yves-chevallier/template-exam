from __future__ import annotations

from texsmith_template_exam.exam import styles


class _DummyContext:
    def __init__(self, runtime: dict[str, object] | None = None) -> None:
        self.runtime = runtime or {}


def test_choice_style_defaults_and_aliases() -> None:
    ctx = _DummyContext({"template_overrides": {"style": {"choices": "checkboxes"}}})
    assert styles.choice_style(ctx) == "checkbox"


def test_text_style_defaults_and_aliases() -> None:
    ctx = _DummyContext({"template_overrides": {"style": {"text": "line"}}})
    assert styles.text_style(ctx) == "lines"
