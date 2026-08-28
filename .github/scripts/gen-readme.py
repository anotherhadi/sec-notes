#!/usr/bin/env python3
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
README = REPO_ROOT / "README.md"
SKIP_DIRS = {".git", ".github", ".direnv"}
SECTION_TITLE_OVERRIDES = {"osint": "OSINT"}
DESCRIPTION = "A personal collection of security notes and cheatsheets, covering offensive security and OSINT."

FRONTMATTER_RE = re.compile(r"^---\n(.*?\n)---\n", re.DOTALL)
FIELD_RE = re.compile(r'^(\w+):\s*"?(.*?)"?\s*$')
TOC_START = (
    "<!-- START doctoc generated TOC please keep comment here to allow auto update -->"
)
TOC_END = (
    "<!-- END doctoc generated TOC please keep comment here to allow auto update -->"
)


def existing_toc_block():
    if README.exists():
        text = README.read_text()
        if TOC_START in text and TOC_END in text:
            start = text.index(TOC_START)
            end = text.index(TOC_END) + len(TOC_END)
            return text[start:end]
    return "[toc]"


def parse_frontmatter(path):
    text = path.read_text()
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        field_match = FIELD_RE.match(line)
        if field_match:
            fields[field_match.group(1)] = field_match.group(2)
    return fields


def section_title(dirname):
    return SECTION_TITLE_OVERRIDES.get(dirname, dirname.capitalize())


def build_section(directory):
    lines = [f"## {section_title(directory.name)}", ""]
    for md_file in sorted(directory.glob("*.md")):
        fields = parse_frontmatter(md_file)
        title = fields.get("title", md_file.stem)
        description = fields.get("description", "")
        rel_path = f"./{directory.name}/{md_file.name}"
        lines.append(f"- [{title}]({rel_path}): {description}")
    lines.append("")
    return lines


def main():
    directories = sorted(
        d
        for d in REPO_ROOT.iterdir()
        if d.is_dir() and d.name not in SKIP_DIRS and any(d.glob("*.md"))
    )

    lines = [
        "# Sec Notes",
        "",
        DESCRIPTION,
        "",
        existing_toc_block(),
        "",
    ]
    for directory in directories:
        lines.extend(build_section(directory))

    README.write_text("\n".join(lines).rstrip("\n") + "\n")


if __name__ == "__main__":
    main()
