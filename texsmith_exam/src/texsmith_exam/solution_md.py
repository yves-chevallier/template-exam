"""Backward-compatible shim for the bundled solution Markdown extension."""

from __future__ import annotations

from texsmith_template_exam.solution_md import SolutionAdmonitionExtension, makeExtension


__all__ = ["SolutionAdmonitionExtension", "makeExtension"]
