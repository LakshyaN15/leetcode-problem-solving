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
    """
    Read 'Key: value' lines from the leading comment block (any comment style).

    'Approach' is special: it is multi-line. Once we see '# Approach:', every
    following comment line is appended to the approach (so a multi-step write-up
    comes through in full) until the header ends.
    """
    KNOWN = {"title", "link", "difficulty", "topics", "tc", "sc", "number", "no", "approach"}
    fields = {}
    in_approach = False
    approach_lines = []
    for line in text.splitlines()[:40]:
        s = line.strip()
        if s == "":
            continue
        if s[0] not in "#/*":                  # hit real code -> header done
            break
        body = s.lstrip("#/*  \t")
        m = re.match(r"([A-Za-z ]+?)\s*:\s*(.*)", body)
        key = m.group(1).strip().lower() if m else None

        if key == "approach":
            in_approach = True
            if m.group(2).strip():
                approach_lines.append(m.group(2).strip())
            continue

        # A new KNOWN key ends the approach block; anything else while in
        # approach mode is treated as a continuation line.
        if in_approach and key not in KNOWN:
            approach_lines.append(body.strip())
            continue
        else:
            in_approach = False

        if m and key in KNOWN:
            fields[key] = m.group(2).strip()

    if approach_lines:
        fields["approach"] = " ".join(approach_lines)
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


# Matches a comment line starting an approach block. Only the exact word
# "Approach" (case-insensitive); the space and colon are optional.
APPROACH_START = re.compile(r"^\s*[#/*]+\s*approach\s*:?\s*(.*)$", re.IGNORECASE)
# These header keys, if seen on their own line, should NOT be folded into an approach
HEADER_KEYS = re.compile(
    r"^\s*[#/*]+\s*(title|link|difficulty|topics|number|no)\s*:", re.IGNORECASE
)


def collect_approaches(text: str) -> str:
    """
    Find EVERY approach block anywhere in the file (not just the header) and
    combine them. Each block runs from its 'Approach:' line through the
    following comment lines, stopping at a blank line, a real code line, or a
    new header key. Blocks are numbered/joined into one cell.
    """
    blocks = []
    lines = text.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        m = APPROACH_START.match(lines[i])
        if not m:
            i += 1
            continue
        parts = []
        if m.group(1).strip():
            parts.append(m.group(1).strip())
        i += 1
        # gather continuation comment lines
        while i < n:
            s = lines[i].strip()
            if s == "":
                break                       # blank line ends the block
            if s[0] not in "#/*":
                break                       # real code ends the block
            if HEADER_KEYS.match(lines[i]) or APPROACH_START.match(lines[i]):
                break                       # next key / next approach ends it
            parts.append(s.lstrip("#/*  \t").strip())
            i += 1
        if parts:
            blocks.append(" ".join(parts))
    return "  •  ".join(blocks)             # separate multiple approaches clearly


def build_problem(key: str, code_files: list, readme_texts: list, topic_dir: Path) -> dict:
    header = {}
    blob = ""
    approach = ""
    for f in code_files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            text = ""
        blob += "\n" + text[:4000]
        if not header:
            h = parse_header(text)
            if h:
                header = h
        if not approach:
            approach = collect_approaches(text)
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
        "approach": approach or header.get("approach", "—"),
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