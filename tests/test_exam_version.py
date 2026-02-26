from __future__ import annotations

from pathlib import Path
import warnings

from texsmith_template_exam.exam import __init__ as exam_mod


def _reset_git_cache() -> None:
    exam_mod._GIT_VERSION = None
    exam_mod._GIT_VERSION_READY = False


def test_exam_version_passes_through_string() -> None:
    _reset_git_cache()
    assert exam_mod._format_exam_version("v1.2.1") == "v1.2.1"
    assert exam_mod._format_exam_version("  custom  ") == "custom"


def test_exam_version_empty_is_blank() -> None:
    _reset_git_cache()
    assert exam_mod._format_exam_version(None) == ""
    assert exam_mod._format_exam_version("") == ""
    assert exam_mod._format_exam_version("   ") == ""


def test_exam_version_git_uses_describe(monkeypatch) -> None:
    _reset_git_cache()

    def _fake_root() -> Path:
        return Path("/tmp/repo")

    def _fake_run(_root: Path, args: list[str]) -> str:
        if args[:2] == ["describe", "--tags"]:
            return "v2.0.0"
        return ""

    monkeypatch.setattr(exam_mod, "_resolve_git_root", _fake_root)
    monkeypatch.setattr(exam_mod, "_run_git", _fake_run)
    assert exam_mod._format_exam_version("git") == "v2.0.0"


def test_exam_version_git_falls_back_to_commit(monkeypatch) -> None:
    _reset_git_cache()

    def _fake_root() -> Path:
        return Path("/tmp/repo")

    def _fake_run(_root: Path, args: list[str]) -> str:
        if args[:2] == ["describe", "--tags"]:
            return ""
        if args[:1] == ["rev-parse"]:
            return "abc123"
        return ""

    monkeypatch.setattr(exam_mod, "_resolve_git_root", _fake_root)
    monkeypatch.setattr(exam_mod, "_run_git", _fake_run)
    assert exam_mod._format_exam_version("git") == "abc123"


def test_exam_version_git_warns_without_repo(monkeypatch) -> None:
    _reset_git_cache()
    monkeypatch.setattr(exam_mod, "_resolve_git_root", lambda: None)
    with warnings.catch_warnings(record=True) as records:
        warnings.simplefilter("always")
        assert exam_mod._format_exam_version("git") == ""
        assert any("version=git requested but no git repository was found" in str(w.message) for w in records)
