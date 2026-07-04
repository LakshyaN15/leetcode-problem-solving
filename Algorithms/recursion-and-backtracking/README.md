# Recursion & Backtracking

**LeetCode tags covered here:** Recursion, Backtracking, Divide and Conquer

Solutions in this bucket:

<!-- - [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/) — Easy -->

<!-- PROBLEMS:START -->
| # | Problem | Difficulty | Topics | Approach | Solution |
|---|---------|:----------:|--------|----------|:--------:|
| 1 | [Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 Easy | Array, Hash Table, Divide and Conquer, Sorting, Counting | 1. Brute Force -> Using nested loop or count=sum(1 for i in nums if i==num), adds 1 for every element found and > 1 (Time Limit Exceeded)<br>TC: O(n^2)<br>SC: O(1) class Solution: def majorityElement(self, nums: List[int]) -> int: n=len(nums) for num in nums: count=sum(1 for i in nums if i==num) if count>n//2: return num<br>2. Hash Map -> declare a defaultdictionary<br>TC: O(n)<br>SC: O(n) | [Python](169-majority-element/majority-element.py) |
<!-- PROBLEMS:END -->
