"""Backward-compatible shim for the bundled exam renderer."""

from __future__ import annotations

from texsmith_template_exam.exam_renderer import register

__all__ = ["register"]
