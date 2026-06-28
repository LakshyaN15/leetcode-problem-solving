#!/usr/bin/env python3
"""
Update the root README stats (badges + Data Structures / Algorithms tables).
Counts unique PROBLEMS (across all languages), not individual files.

Run from repo root:
    python scripts/update_readme.py
"""
import re
from _common import ROOT, DS_PARENTS, ALGO_PARENTS, topic_problems, DIFF_EMOJI

README = ROOT / "README.md"
SQL_PARENT = "SQL"


def scan(parents):
    rows, tot = [], {"Easy": 0, "Medium": 0, "Hard": 0, "Solved": 0}
    for parent in parents:
        base = ROOT / parent
        if not base.exists():
            continue
        for topic in sorted(p for p in base.iterdir() if p.is_dir()):
            probs = topic_problems(topic)
            c = {"Easy": 0, "Medium": 0, "Hard": 0}
            for p in probs:
                if p["diff"] in c:
                    c[p["diff"]] += 1
            link = f"{parent.replace(' ', '%20')}/{topic.name}"
            rows.append((topic.name, link, c["Easy"], c["Medium"], c["Hard"], len(probs)))
            for k in c:
                tot[k] += c[k]
            tot["Solved"] += len(probs)
    return rows, tot


def scan_flat(parent):
    """Count problems in a flat folder (e.g. SQL synced by LeetSync), no topic buckets."""
    base = ROOT / parent
    tot = {"Easy": 0, "Medium": 0, "Hard": 0, "Solved": 0}
    if not base.exists():
        return tot
    probs = topic_problems(base)
    for p in probs:
        if p["diff"] in tot:
            tot[p["diff"]] += 1
        tot["Solved"] += 1
    return tot


def table(rows, tot):
    out = [
        "| Topic | Folder | 🟢 Easy | 🟡 Med | 🔴 Hard | Solved |",
        "|-------|--------|:------:|:------:|:------:|:------:|",
    ]
    for name, link, e, m, h, s in rows:
        nice = name.replace("-", " ").title()
        out.append(f"| {nice} | [{name}]({link}) | {e} | {m} | {h} | {s} |")
    out.append(
        f"| **Total** | | **{tot['Easy']}** | **{tot['Medium']}** | **{tot['Hard']}** | **{tot['Solved']}** |"
    )
    return "\n".join(out)


def badges(g):
    def b(label, val, color):
        return f"![{label}](https://img.shields.io/badge/{label}-{val}-{color})"
    return " ".join([
        b("Solved", g["Solved"], "blue"),
        b("Easy", g["Easy"], "brightgreen"),
        b("Medium", g["Medium"], "orange"),
        b("Hard", g["Hard"], "red"),
    ])


def replace_block(content, name, new):
    s, e = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    pat = re.compile(re.escape(s) + r".*?" + re.escape(e), re.DOTALL)
    if not pat.search(content):
        raise SystemExit(f"Marker {s} ... {e} not found in root README.md")
    return pat.sub(f"{s}\n{new}\n{e}", content)


def sql_table(parent, tot):
    return "\n".join([
        "| Category | Folder | 🟢 Easy | 🟡 Med | 🔴 Hard | Solved |",
        "|----------|--------|:------:|:------:|:------:|:------:|",
        f"| SQL | [{parent}]({parent}) | {tot['Easy']} | {tot['Medium']} | {tot['Hard']} | {tot['Solved']} |",
    ])


def main():
    ds_rows, ds_tot = scan(DS_PARENTS)
    al_rows, al_tot = scan(ALGO_PARENTS)
    sql_tot = scan_flat(SQL_PARENT)
    grand = {k: ds_tot[k] + al_tot[k] + sql_tot[k] for k in ds_tot}

    content = README.read_text(encoding="utf-8")
    content = replace_block(content, "BADGES", badges(grand))
    content = replace_block(content, "DS", table(ds_rows, ds_tot))
    content = replace_block(content, "ALGO", table(al_rows, al_tot))
    content = replace_block(content, "SQL", sql_table(SQL_PARENT, sql_tot))
    README.write_text(content, encoding="utf-8")
    print(f"Root README updated — {grand['Solved']} solved "
          f"({grand['Easy']}E / {grand['Medium']}M / {grand['Hard']}H), "
          f"SQL: {sql_tot['Solved']}")


if __name__ == "__main__":
    main()