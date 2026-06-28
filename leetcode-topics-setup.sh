#!/usr/bin/env bash
# LeetCode topic-wise scaffolder — topics split into data-structures/ and algorithms/.
# Usage: bash leetcode-topics-setup.sh   (run from your repo root)

set -e

# Data-structure topics
ds_topics=(
  "array"
  "string"
  "hash-table"
  "linked-list"
  "stack"
  "queue"
  "tree"
  "bst"
  "heap"
  "graph"
  "trie"
  "matrix"
  "union-find"
)

# Algorithm / technique topics
algo_topics=(
  "two-pointers"
  "sliding-window"
  "prefix-sum"
  "binary-search"
  "sorting"
  "recursion"
  "divide-and-conquer"
  "backtracking"
  "dfs"
  "bfs"
  "dynamic-programming"
  "greedy"
  "intervals"
  "monotonic-stack"
  "bit-manipulation"
  "math"
  "design"
)

make_topic () {
  local parent="$1" topic="$2"
  local dir="$parent/$topic"
  mkdir -p "$dir"
  local title
  title=$(echo "$topic" | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)}1')
  printf "# %s\n\nProblems solved in this topic:\n\n<!-- - [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/) — Easy -->\n" "$title" > "$dir/README.md"
  echo "Created $dir/"
}

for t in "${ds_topics[@]}";   do make_topic "Data Structures" "$t"; done
for t in "${algo_topics[@]}"; do make_topic "Algorithms"      "$t"; done

# Parent-folder READMEs
printf "# 📦 Data Structures\n\nLeetCode solutions grouped by data-structure topic.\n" > "Data Structures/README.md"
printf "# ⚙️ Algorithms & Techniques\n\nLeetCode solutions grouped by algorithm/technique.\n" > "Algorithms/README.md"

total=$(( ${#ds_topics[@]} + ${#algo_topics[@]} ))
echo ""
echo "✅ Created $total topic folders ( ${#ds_topics[@]} data-structures, ${#algo_topics[@]} algorithms )."
echo "Now run:"
echo "   git add . && git commit -m 'Scaffold LeetCode topic folders' && git push"