#!/usr/bin/env python3
"""
Build a problems table inside EVERY folder's README from solution file headers.

Run from repo root:
    python scripts/update_folders.py

For each topic folder under the parent folders below, it reads every solution
(.py) file's header, extracts the fields, and writes a table between the
<!-- PROBLEMS:START --> / <!-- PROBLEMS:END --> markers in that folder's README.md.

Each solution file should start with a header like:

    # Title: Two Sum
    # Link: https://leetcode.com/problems/two-sum/
    # Difficulty: Easy
    # Topics: Array, Hash Table
    # TC: O(n)
    # SC: O(n)

The LeetCode problem number is taken from the filename prefix (e.g. 0001-...).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARENTS = ["Data Structures", "Algorithms", "Database"]

START, END = "<!-- PROBLEMS:START -->", "<!-- PROBLEMS:END -->"
DIFF_EMOJI = {"Easy": "🟢 Easy", "Medium": "🟡 Medium", "Hard": "🔴 Hard"}


def parse_header(path: Path) -> dict:
    """Pull '# Key: value' lines from the top of a file into a dict."""
    fields = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        s = line.strip()
        if not s.startswith("#"):
            # stop scanning once we leave the header comment block
            if s == "":
                continue
            break
        m = re.match(r"#\s*([A-Za-z ]+?)\s*:\s*(.+)", s)
        if m:
            fields[m.group(1).strip().lower()] = m.group(2).strip()
    return fields


def number_from_name(name: str) -> str:
    """Extract leading problem number from e.g. '0015-3sum.py' -> '15'."""
    m = re.match(r"0*(\d+)", name)
    return m.group(1) if m else ""


def is_solution(f: Path) -> bool:
    return (
        f.suffix == ".py"
        and not f.name.startswith(("test_", "_"))
        and f.name != "conftest.py"
    )


def build_table(folder: Path) -> str:
    rows = []
    for f in sorted(folder.glob("*.py")):
        if not is_solution(f):
            continue
        h = parse_header(f)
        num = number_from_name(f.name)
        title = h.get("title", f.stem)
        link = h.get("link", "")
        problem = f"[{title}]({link})" if link else title
        diff = DIFF_EMOJI.get(h.get("difficulty", ""), h.get("difficulty", "—"))
        topics = h.get("topics", "—")
        tc = h.get("tc", "—")
        sc = h.get("sc", "—")
        # link to the solution file itself, relative to this folder's README
        solution = f"[code]({f.name.replace(' ', '%20')})"
        rows.append((int(num) if num else 0, num, problem, diff, topics, tc, sc, solution))

    rows.sort(key=lambda r: r[0])
    if not rows:
        return "_No problems yet._"

    lines = [
        "| # | Problem | Difficulty | Topics | TC | SC | Solution |",
        "|---|---------|:----------:|--------|----|----|:--------:|",
    ]
    for _, num, problem, diff, topics, tc, sc, solution in rows:
        lines.append(f"| {num} | {problem} | {diff} | {topics} | {tc} | {sc} | {solution} |")
    return "\n".join(lines)


def update_folder_readme(folder: Path):
    readme = folder / "README.md"
    if not readme.exists():
        return False
    content = readme.read_text(encoding="utf-8")
    if START not in content or END not in content:
        return False
    table = build_table(folder)
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    new = pat.sub(f"{START}\n{table}\n{END}", content)
    if new != content:
        readme.write_text(new, encoding="utf-8")
    return True


def main():
    updated = 0
    for parent in PARENTS:
        base = ROOT / parent
        if not base.exists():
            continue
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            if update_folder_readme(folder):
                updated += 1
    print(f"Updated problem tables in {updated} folder README(s).")


if __name__ == "__main__":
    main()
