"""Custom template hooks for the exam template."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from texsmith.adapters.latex.renderer import LaTeXRenderer
from texsmith.adapters.markdown import DEFAULT_MARKDOWN_EXTENSIONS, render_markdown
from texsmith.core.templates.base import WrappableTemplate


_RENDERER: LaTeXRenderer | None = None


def _markdown_to_latex(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    if not text.strip():
        return text
    html = render_markdown(text, DEFAULT_MARKDOWN_EXTENSIONS).html
    global _RENDERER
    if _RENDERER is None:
        _RENDERER = LaTeXRenderer(copy_assets=False, convert_assets=False)
    return _RENDERER.render(html).strip()


class Template(WrappableTemplate):
    """Exam template with extra Jinja filters."""

    def __init__(self) -> None:
        super().__init__(Path(__file__).resolve().parent)
        self.environment.filters.setdefault("markdown_to_latex", _markdown_to_latex)
