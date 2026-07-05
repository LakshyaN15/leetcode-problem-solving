# Recursion & Backtracking

**LeetCode tags covered here:** Recursion, Backtracking, Divide and Conquer

Solutions in this bucket:

<!-- - [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/) — Easy -->

<!-- PROBLEMS:START -->
| # | Problem | Difficulty | Topics | Approach | Solution |
|---|---------|:----------:|--------|----------|:--------:|
| 1 | [Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 Easy | Array, Hash Table, Divide and Conquer, Sorting, Counting | 1. Brute Force -> Using nested loop or count=sum(1 for i in nums if i==num), adds 1 for every element found and > 1 (Time Limit Exceeded)<br>TC: O(n^2)<br>SC: O(1) class Solution: def majorityElement(self, nums: List[int]) -> int: n=len(nums) for num in nums: count=sum(1 for i in nums if i==num) if count>n//2: return num<br>2. Hash Map -> declare a defaultdict(int) - a special dictionary that auto-creates missing keys with a default value — and for int, that default is 0. This means you can do count[num] += 1 directly, even the very first time you see num, without ever getting a KeyError, delacre maxCount=res=0 and check if maxCount<count[num], if yes then res=num and maxCount=count[num]. Return max appeared num in end as res<br>TC: O(n)<br>SC: O(n) class Solution: def majorityElement(self, nums: List[int]) -> int: count=defaultdict(int) res=maxCount=0<br>3. Sorting -> Approach is to sort as after sort majority element will occupy middle pos no matter what.<br>TC: O(nlogn)<br>SC: O(1) or O(n) depending on sorting algo class Solution: def majorityElement(self, nums: List[int]) -> int: nums.sort() return nums[len(nums)//2]<br>4. Booye Moore -> The Boyer-Moore algorithm works by maintaining a candidate and a count. When we see the candidate, we increment the count; otherwise, we decrement it. When the count reaches 0, we pick a new candidate. Since the majority element appears more than half the time, it will survive this elimination process and remain as the final candidate.<br>TC: O(n)<br>SC: O(1)<br>5. Bit Manipulation -> (will cover later)<br>TC: O(n*32)<br>SC: O(32) | [Python](169-majority-element/majority-element.py) |
<!-- PROBLEMS:END -->
