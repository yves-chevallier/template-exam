"""Local TeXSmith extensions for the exam template."""

from __future__ import annotations

from re import Match
import re
import xml.etree.ElementTree as ElementTree

from markdown import Extension, Markdown
from markdown.inlinepatterns import InlineProcessor
from markdown.util import AtomicString

_FILLIN_PATTERN = r"\[([^\]\n]+)\]\{([^}\n]+)\}"
_FILLIN_WIDTH_PATTERN = re.compile(r"\b(?:w|width)\s*=\s*([^\s,}]+)")


class _FillInInlineProcessor(InlineProcessor):
    """Convert [answer]{w=50} into a texsmith fill-in span."""

    def handleMatch(  # type: ignore[override]  # noqa: N802
        self,
        match: Match[str],
        data: str,
    ) -> tuple[ElementTree.Element, int, int]:
        answer = match.group(1)
        attrs = match.group(2)
        width_value = ""
        width_match = _FILLIN_WIDTH_PATTERN.search(attrs)
        if width_match:
            width_value = width_match.group(1)

        element = ElementTree.Element("span")
        element.set("class", "texsmith-fillin")
        if width_value:
            element.set("data-width", width_value)
        element.text = AtomicString(answer)
        return element, match.start(0), match.end(0)


class TexsmithExamExtension(Extension):
    """Register the exam-specific Markdown inline processors."""

    def extendMarkdown(self, md: Markdown) -> None:  # type: ignore[override]  # noqa: N802
        processor = _FillInInlineProcessor(_FILLIN_PATTERN, md)
        md.inlinePatterns.register(processor, "texsmith_exam_fillin", 85)


def makeExtension(**kwargs: object) -> TexsmithExamExtension:  # noqa: N802
    return TexsmithExamExtension(**kwargs)


__all__ = ["TexsmithExamExtension", "makeExtension"]
