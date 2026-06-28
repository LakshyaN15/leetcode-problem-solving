#!/usr/bin/env python3
"""
Auto-update the root README with per-topic solution counts.

Run from the repo root:
    python scripts/update_readme.py

It scans the "Data Structures" and "Algorithms" parent folders, counts the
solution files in each topic subfolder, reads each file's difficulty from its
header comment, and rewrites the marked blocks in README.md.

Markers it fills (must exist in README.md):
    <!-- BADGES:START --> ... <!-- BADGES:END -->
    <!-- DS:START -->     ... <!-- DS:END -->
    <!-- ALGO:START -->   ... <!-- ALGO:END -->
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

PARENTS = {"DS": "Data Structures", "ALGO": "Algorithms"}
DIFF_RE = re.compile(r"\b(Easy|Medium|Hard)\b", re.IGNORECASE)


def detect_difficulty(path: Path):
    """Return 'Easy' | 'Medium' | 'Hard' from the file header, or None."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    m = DIFF_RE.search(text)
    return m.group(1).capitalize() if m else None


def is_solution(f: Path) -> bool:
    """A .py file that is a solution (not a test/helper)."""
    if f.suffix != ".py":
        return False
    return not (f.name.startswith(("test_", "_")) or f.name == "conftest.py")


def scan(parent: str):
    base = ROOT / parent
    rows, totals = [], {"Easy": 0, "Medium": 0, "Hard": 0, "Solved": 0}
    if not base.exists():
        return rows, totals
    for topic in sorted(p for p in base.iterdir() if p.is_dir()):
        c = {"Easy": 0, "Medium": 0, "Hard": 0}
        solved = 0
        for f in topic.iterdir():
            if not is_solution(f):
                continue
            solved += 1
            d = detect_difficulty(f)
            if d in c:
                c[d] += 1
        link = f"{parent.replace(' ', '%20')}/{topic.name}"
        rows.append((topic.name, link, c["Easy"], c["Medium"], c["Hard"], solved))
        for k in c:
            totals[k] += c[k]
        totals["Solved"] += solved
    return rows, totals


def build_table(rows, totals):
    lines = [
        "| Topic | Folder | 🟢 Easy | 🟡 Med | 🔴 Hard | Solved |",
        "|-------|--------|:------:|:------:|:------:|:------:|",
    ]
    for name, link, e, m, h, s in rows:
        nice = name.replace("-", " ").title()
        lines.append(f"| {nice} | [{name}]({link}) | {e} | {m} | {h} | {s} |")
    lines.append(
        f"| **Total** | | **{totals['Easy']}** | **{totals['Medium']}** "
        f"| **{totals['Hard']}** | **{totals['Solved']}** |"
    )
    return "\n".join(lines)


def build_badges(g):
    def badge(label, val, color):
        return f"![{label}](https://img.shields.io/badge/{label}-{val}-{color})"
    return " ".join([
        badge("Solved", g["Solved"], "blue"),
        badge("Easy", g["Easy"], "brightgreen"),
        badge("Medium", g["Medium"], "orange"),
        badge("Hard", g["Hard"], "red"),
    ])


def replace_block(content: str, name: str, new: str) -> str:
    start, end = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pat.search(content):
        raise SystemExit(f"Marker {start} ... {end} not found in README.md")
    return pat.sub(f"{start}\n{new}\n{end}", content)


def main():
    ds_rows, ds_tot = scan(PARENTS["DS"])
    al_rows, al_tot = scan(PARENTS["ALGO"])
    grand = {k: ds_tot[k] + al_tot[k] for k in ds_tot}

    content = README.read_text(encoding="utf-8")
    content = replace_block(content, "BADGES", build_badges(grand))
    content = replace_block(content, "DS", build_table(ds_rows, ds_tot))
    content = replace_block(content, "ALGO", build_table(al_rows, al_tot))
    README.write_text(content, encoding="utf-8")
    print(f"README updated — {grand['Solved']} solved "
          f"({grand['Easy']}E / {grand['Medium']}M / {grand['Hard']}H)")


if __name__ == "__main__":
    main()