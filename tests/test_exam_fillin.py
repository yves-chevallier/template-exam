from __future__ import annotations

from texsmith_template_exam.exam import fillin


class _DummyContext:
    def __init__(self, runtime: dict[str, object] | None = None) -> None:
        self.runtime = runtime or {}


def test_compute_fillin_width_prefers_explicit_width() -> None:
    ctx = _DummyContext()
    width = fillin.compute_fillin_width(answer_raw="42", attrs="width=30mm", context=ctx)
    assert width == "30mm"


def test_build_fillin_latex_solution_mode_drops_width() -> None:
    ctx = _DummyContext({"template_overrides": {"solution": True}})
    latex = fillin.build_fillin_latex(
        answer_raw="42",
        answer_latex="42",
        attrs="width=30mm",
        context=ctx,
        solution_mode=True,
    )
    assert latex == r"\fillin[42]"
