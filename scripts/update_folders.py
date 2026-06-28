#!/usr/bin/env python3
"""
Build a problems table inside every topic folder's README.

Works with hand-written headers AND LeetSync files (any language, nested folders,
no header). If a folder README is missing the PROBLEMS markers, they are added
automatically.

Run from repo root:
    python scripts/update_folders.py
"""
import re
from _common import (
    ROOT, ALL_PARENTS, START, END, DIFF_EMOJI, topic_problems,
)


def build_table(topic_dir):
    probs = topic_problems(topic_dir)
    if not probs:
        return "_No problems yet._"
    lines = [
        "| # | Problem | Difficulty | Topics | TC | SC | Approach | Solution |",
        "|---|---------|:----------:|--------|----|----|----------|:--------:|",
    ]
    for p in probs:
        num = p["num"] if p["num"] is not None else ""
        problem = f"[{p['title']}]({p['link']})" if p["link"] else p["title"]
        diff = DIFF_EMOJI.get(p["diff"], p["diff"] or "—")
        approach = (p["approach"] or "—").replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {num} | {problem} | {diff} | {p['topics']} | {p['tc']} | {p['sc']} | {approach} | {p['solution']} |"
        )
    return "\n".join(lines)


def update_folder_readme(folder):
    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(f"# {folder.name}\n\n{START}\n{END}\n", encoding="utf-8")
    content = readme.read_text(encoding="utf-8")
    if START not in content or END not in content:
        content = content.rstrip() + f"\n\n{START}\n{END}\n"
    table = build_table(folder)
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    new = pat.sub(f"{START}\n{table}\n{END}", content)
    if new != content:
        readme.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    updated = 0
    for parent in ALL_PARENTS:
        base = ROOT / parent
        if not base.exists():
            continue
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            if update_folder_readme(folder):
                updated += 1
    print(f"Updated problem tables in {updated} folder README(s).")


if __name__ == "__main__":
    main()