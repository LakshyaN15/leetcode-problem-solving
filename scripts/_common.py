#!/usr/bin/env python3
"""
Shared helpers for the README scripts.

Handles a MIX of:
  - hand-written files with a header (# Title: / # Link: / # Difficulty: / # Topics: / # TC: / # SC:)
  - LeetSync-style files: any language, often in a per-problem subfolder, no header.

A "problem" is either a code file sitting directly in a topic folder, or a
per-problem subfolder containing one or more code files (multiple languages).
"""
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

# Parent folders that hold topic buckets
DS_PARENTS = ["Data Structures"]
ALGO_PARENTS = ["Algorithms"]
ALL_PARENTS = ["Data Structures", "Algorithms", "Database", "SQL"]

START, END = "<!-- PROBLEMS:START -->", "<!-- PROBLEMS:END -->"
DIFF_EMOJI = {"Easy": "🟢 Easy", "Medium": "🟡 Medium", "Hard": "🔴 Hard"}
DIFF_RE = re.compile(r"\b(Easy|Medium|Hard)\b")

# Recognised solution languages -> label shown in the Solution column
CODE_EXT = {
    ".py": "Python", ".java": "Java", ".cpp": "C++", ".cc": "C++", ".c": "C",
    ".js": "JS", ".ts": "TS", ".rb": "Ruby", ".go": "Go", ".rs": "Rust",
    ".kt": "Kotlin", ".swift": "Swift", ".scala": "Scala", ".lua": "Lua",
    ".cs": "C#", ".php": "PHP", ".sql": "SQL", ".dart": "Dart",
}


def is_code(f: Path) -> bool:
    return (
        f.suffix.lower() in CODE_EXT
        and not f.name.startswith(("test_", "_"))
        and f.name != "conftest.py"
    )


def parse_header(text: str) -> dict:
    """Read 'Key: value' lines from the leading comment block (any comment style)."""
    fields = {}
    for line in text.splitlines()[:25]:
        s = line.strip()
        if s == "":
            continue
        if s[0] in "#/*":                      # a comment line
            s2 = s.lstrip("#/*  \t")
            m = re.match(r"([A-Za-z ]+?)\s*:\s*(.+)", s2)
            if m:
                fields[m.group(1).strip().lower()] = m.group(2).strip()
        else:
            break                              # hit real code -> header done
    return fields


def split_key(key: str):
    """'0011-container-with-most-water' -> (11, 'container-with-most-water')."""
    m = re.match(r"0*(\d+)[-_ ]+(.*)", key)
    if m:
        return int(m.group(1)), m.group(2).strip("-_ ").lower().replace("_", "-").replace(" ", "-")
    m2 = re.match(r"0*(\d+)$", key)
    if m2:
        return int(m2.group(1)), ""
    return None, key.strip("-_ ").lower().replace("_", "-").replace(" ", "-")


def title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").title() if slug else "Untitled"


def build_problem(key: str, code_files: list, readme_texts: list, topic_dir: Path) -> dict:
    header = {}
    blob = ""
    for f in code_files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            text = ""
        blob += "\n" + text[:2000]
        if not header:
            h = parse_header(text)
            if h:
                header = h
    for t in readme_texts:
        blob += "\n" + t[:2000]

    num, slug = split_key(key)
    title = header.get("title") or title_from_slug(slug)
    link = header.get("link")
    if not link and slug:
        link = f"https://leetcode.com/problems/{slug}/"

    diff = header.get("difficulty", "")
    if not diff:
        m = DIFF_RE.search(blob)
        diff = m.group(1) if m else ""

    if num is None:
        n = header.get("number") or header.get("no") or ""
        num = int(n) if str(n).isdigit() else None

    sol = []
    for f in sorted(code_files):
        lang = CODE_EXT.get(f.suffix.lower(), "code")
        rel = quote(f.relative_to(topic_dir).as_posix())
        sol.append(f"[{lang}]({rel})")

    return {
        "num": num,
        "title": title,
        "link": link,
        "diff": diff,
        "topics": header.get("topics", "—"),
        "tc": header.get("tc", "—"),
        "sc": header.get("sc", "—"),
        "approach": header.get("approach", "—"),
        "solution": " ".join(sol),
    }


def topic_problems(topic_dir: Path) -> list:
    """Return a list of problem dicts for one topic folder."""
    problems = []
    for child in sorted(topic_dir.iterdir()):
        if child.name.lower() == "readme.md":
            continue
        if child.is_file() and is_code(child):
            problems.append(build_problem(child.stem, [child], [], topic_dir))
        elif child.is_dir():
            code_files = [f for f in child.rglob("*") if f.is_file() and is_code(f)]
            readmes = [
                f.read_text(encoding="utf-8", errors="ignore")
                for f in child.rglob("*")
                if f.name.lower() == "readme.md"
            ]
            if code_files:
                problems.append(build_problem(child.name, code_files, readmes, topic_dir))
    problems.sort(key=lambda p: (p["num"] is None, p["num"] or 0, p["title"]))
    return problems
