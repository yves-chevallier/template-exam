"""Shared style helpers for exam rendering."""

from __future__ import annotations

from texsmith.core.context import RenderContext

from texsmith_template_exam.exam.utils import normalize_style_choice


def exam_style(context: RenderContext) -> dict[str, object]:
    overrides = context.runtime.get("template_overrides")
    if not isinstance(overrides, dict):
        return {}
    style = overrides.get("style")
    return style if isinstance(style, dict) else {}


def choice_style(context: RenderContext) -> str:
    style = exam_style(context)
    return normalize_style_choice(
        style.get("choices"),
        default="alpha",
        aliases={"checkboxes": "checkbox", "check": "checkbox"},
    )


def text_style(context: RenderContext) -> str:
    style = exam_style(context)
    return normalize_style_choice(
        style.get("text"),
        default="dotted",
        aliases={"dots": "dotted", "dottedlines": "dotted", "line": "lines"},
    )


__all__ = ["choice_style", "exam_style", "text_style"]
