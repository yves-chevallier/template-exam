from __future__ import annotations

from texsmith_template_exam.exam import mode


class _DummyContext:
    def __init__(self, runtime: dict[str, object] | None = None) -> None:
        self.runtime = runtime or {}


def test_in_solution_mode_from_overrides_and_path_fallback() -> None:
    assert mode.in_solution_mode(_DummyContext({"template_overrides": {"solution": True}}))
    assert mode.in_solution_mode(_DummyContext({"solution": "true"}))
    assert mode.in_solution_mode(
        _DummyContext({"document_path": "/tmp/build/series/20/solution/series-20.md"})
    )
    assert not mode.in_solution_mode(_DummyContext())


def test_in_compact_mode_from_overrides_and_path_fallback() -> None:
    assert mode.in_compact_mode(_DummyContext({"template_overrides": {"compact": True}}))
    assert mode.in_compact_mode(_DummyContext({"compact": "yes"}))
    assert mode.in_compact_mode(
        _DummyContext({"document_path": "/tmp/build/series/20/light-src/series-20.md"})
    )
    assert not mode.in_compact_mode(_DummyContext())
