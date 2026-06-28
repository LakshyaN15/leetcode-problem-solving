#!/usr/bin/env bash
# Scaffold a complete bucket structure covering EVERY LeetCode tag.
# Granular tags are grouped under their broad home (e.g. Sliding Window -> Arrays).
# Each bucket's README lists exactly which LeetCode tags it absorbs.
# Usage: bash scaffold-all.sh   (run from repo root)

set -e

# format: parent | folder | Title | comma-separated LeetCode tags it covers
buckets=(
  "Data Structures|arrays|Arrays|Array, Two Pointers, Sliding Window, Prefix Sum, Matrix"
  "Data Structures|strings|Strings|String, String Matching, Rolling Hash, Suffix Array"
  "Data Structures|hashing|Hashing|Hash Table, Hash Function, Counting, Ordered Set"
  "Data Structures|stack-and-queue|Stack & Queue|Stack, Queue, Monotonic Stack, Monotonic Queue"
  "Data Structures|linked-list|Linked List|Linked List, Doubly-Linked List"
  "Data Structures|trees|Trees|Tree, Binary Tree, Binary Search Tree, Trie, Segment Tree, Binary Indexed Tree"
  "Data Structures|heap|Heap / Priority Queue|Heap (Priority Queue)"
  "Data Structures|graphs|Graphs|Graph, Union-Find, Minimum Spanning Tree, Strongly Connected Component, Biconnected Component, Eulerian Circuit"
  "Algorithms|searching-and-sorting|Searching & Sorting|Binary Search, Sorting, Merge Sort, Counting Sort, Radix Sort, Bucket Sort, Quickselect, Shell"
  "Algorithms|graph-traversal|Graph Traversal|Depth-First Search, Breadth-First Search, Topological Sort, Shortest Path"
  "Algorithms|dynamic-programming|Dynamic Programming|Dynamic Programming, Memoization"
  "Algorithms|recursion-and-backtracking|Recursion & Backtracking|Recursion, Backtracking, Divide and Conquer"
  "Algorithms|greedy|Greedy|Greedy, Sweep Line"
  "Algorithms|math|Math|Math, Number Theory, Combinatorics, Geometry, Bit Manipulation, Bitmask, Probability and Statistics, Game Theory, Randomized, Reservoir Sampling, Rejection Sampling"
  "Algorithms|design|Design & Simulation|Design, Data Stream, Iterator, Simulation, Enumeration, Brainteaser, Interactive, Concurrency"
  "Database|database|Database (SQL)|Database"
)

for row in "${buckets[@]}"; do
  IFS='|' read -r parent folder title tags <<< "$row"
  dir="$parent/$folder"
  mkdir -p "$dir"
  {
    printf "# %s\n\n" "$title"
    printf "**LeetCode tags covered here:** %s\n\n" "$tags"
    printf "Solutions in this bucket:\n\n"
    printf "<!-- - [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/) — Easy -->\n"
  } > "$dir/README.md"
  echo "Created $dir/"
done

# parent-folder READMEs
printf "# 📦 Data Structures\n\nSolutions grouped by data-structure bucket.\n" > "Data Structures/README.md"
printf "# ⚙️ Algorithms\n\nSolutions grouped by algorithm bucket.\n" > "Algorithms/README.md"
printf "# 🗄️ Database\n\nSQL solutions.\n" > "Database/README.md"

echo ""
echo "✅ Created ${#buckets[@]} buckets covering all LeetCode tags."