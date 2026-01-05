"""Markdown extension for solution blocks without touching TeXSmith internals."""

from __future__ import annotations

import re

from markdown import Markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


_SOLUTION_PATTERN = re.compile(
    r"^\s*!!!\s+solution(?:\s*\{(?P<attrs>[^}]*)\})?\s*$", re.IGNORECASE
)
_LINES_PATTERN = re.compile(r"\blines\s*=\s*(\d+)\b")


class _SolutionBlockPreprocessor(Preprocessor):
    """Convert solution admonitions into LaTeX environment wrappers."""

    def run(self, lines: list[str]) -> list[str]:
        output: list[str] = []
        index = 0
        total = len(lines)

        while index < total:
            line = lines[index]
            match = _SOLUTION_PATTERN.match(line)
            if not match:
                output.append(line)
                index += 1
                continue

            attrs = match.group("attrs") or ""
            lines_value = None
            if attrs:
                lines_match = _LINES_PATTERN.search(attrs)
                if lines_match:
                    lines_value = lines_match.group(1)

            content: list[str] = []
            index += 1
            while index < total:
                current = lines[index]
                if current.startswith("    "):
                    content.append(current[4:])
                    index += 1
                    continue
                if current.startswith("\t"):
                    content.append(current[1:])
                    index += 1
                    continue
                if current.strip() == "":
                    next_index = index + 1
                    if next_index < total and (
                        lines[next_index].startswith("    ")
                        or lines[next_index].startswith("\t")
                    ):
                        content.append("")
                        index += 1
                        continue
                break

            if not content:
                output.append(line)
                continue

            if lines_value:
                begin_env = (
                    "<p class=\"latex-raw\" style=\"display:none;\">"
                    f"\\begin{{solutionordottedlines}}[{lines_value}"
                    "\\dottedlinefillheight]</p>"
                )
            else:
                begin_env = (
                    "<p class=\"latex-raw\" style=\"display:none;\">"
                    "\\begin{solution}</p>"
                )

            end_env = (
                "<p class=\"latex-raw\" style=\"display:none;\">"
                f"\\end{{solutionordottedlines}}</p>"
                if lines_value
                else "<p class=\"latex-raw\" style=\"display:none;\">\\end{solution}</p>"
            )

            output.append(begin_env)
            output.append('<div class="texsmith-solution" markdown="1">')
            output.extend(content)
            output.append("</div>")
            output.append(end_env)

        return output


class SolutionAdmonitionExtension(Extension):
    """Register the solution block preprocessor."""

    def extendMarkdown(self, md: Markdown) -> None:  # type: ignore[override]  # noqa: N802
        md.preprocessors.register(
            _SolutionBlockPreprocessor(),
            "texsmith_exam_solution",
            priority=30,
        )


def makeExtension(**kwargs: object) -> SolutionAdmonitionExtension:  # noqa: N802
    return SolutionAdmonitionExtension(**kwargs)


__all__ = ["SolutionAdmonitionExtension", "makeExtension"]
