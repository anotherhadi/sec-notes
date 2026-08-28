#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".direnv", ".github"}

TOC_PLACEHOLDER_RE = re.compile(r"\[toc\]", re.IGNORECASE)
TOC_START = "<!-- START doctoc generated TOC please keep comment here to allow auto update -->"
TOC_END = "<!-- END doctoc generated TOC please keep comment here to allow auto update -->"


def find_markdown_files():
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if not SKIP_DIRS.isdisjoint(path.relative_to(REPO_ROOT).parts):
            continue
        yield path


def has_toc_markers(path):
    text = path.read_text()
    if TOC_START in text:
        return True
    if TOC_PLACEHOLDER_RE.search(text):
        text = TOC_PLACEHOLDER_RE.sub(f"{TOC_START}\n{TOC_END}", text, count=1)
        path.write_text(text)
        return True
    return False


def main():
    for md_file in find_markdown_files():
        if has_toc_markers(md_file):
            subprocess.run(["doctoc", "--notitle", str(md_file)], check=True)


if __name__ == "__main__":
    main()
