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
        "| # | Problem | Difficulty | Topics | Approach | Solution |",
        "|---|---------|:----------:|--------|----------|:--------:|",
    ]
    for idx, p in enumerate(probs, start=1):
        problem = f"[{p['title']}]({p['link']})" if p["link"] else p["title"]
        diff = DIFF_EMOJI.get(p["diff"], p["diff"] or "—")
        approach = (p["approach"] or "—").replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {idx} | {problem} | {diff} | {p['topics']} | {approach} | {p['solution']} |"
        )
    return "\n".join(lines)


def build_sql_table(topic_dir):
    """SQL folder table: # | Problem | Difficulty | Solution | Approach (no Topics)."""
    probs = topic_problems(topic_dir)
    if not probs:
        return "_No problems yet._"
    lines = [
        "| # | Problem | Difficulty | Solution | Approach |",
        "|---|---------|:----------:|:--------:|----------|",
    ]
    for idx, p in enumerate(probs, start=1):
        problem = f"[{p['title']}]({p['link']})" if p["link"] else p["title"]
        diff = DIFF_EMOJI.get(p["diff"], p["diff"] or "—")
        approach = (p["approach"] or "—").replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {idx} | {problem} | {diff} | {p['solution']} | {approach} |"
        )
    return "\n".join(lines)


def update_folder_readme(folder, builder=build_table):
    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(f"# {folder.name}\n\n{START}\n{END}\n", encoding="utf-8")
    content = readme.read_text(encoding="utf-8")
    if START not in content or END not in content:
        content = content.rstrip() + f"\n\n{START}\n{END}\n"
    table = builder(folder)
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    new = pat.sub(f"{START}\n{table}\n{END}", content)
    if new != content:
        readme.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    updated = 0
    for parent in ["Data Structures", "Algorithms"]:
        base = ROOT / parent
        if not base.exists():
            continue
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            if update_folder_readme(folder):
                updated += 1

    # SQL folder: flat (no topic buckets) -> build its table directly with the SQL layout
    sql = ROOT / "SQL"
    if sql.exists():
        if update_folder_readme(sql, builder=build_sql_table):
            updated += 1

    print(f"Updated problem tables in {updated} folder README(s).")


if __name__ == "__main__":
    main()