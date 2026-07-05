# Arrays

**LeetCode tags covered here:** Array, Two Pointers, Sliding Window, Prefix Sum, Matrix

Solutions in this bucket:

<!-- - [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/) — Easy -->

<!-- PROBLEMS:START -->
| # | Problem | Difficulty | Topics | Approach | Solution |
|---|---------|:----------:|--------|----------|:--------:|
| 1 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟢 Easy | Array, Hash Table, Sorting | 1. Brute Force -> Declare two var i and j and compare with next, if equal then True else False<br>TC: O(n^2)<br>SC: O(n)<br>2. Sorting -> Sort using nums.sort() then compare from idx 1 to prev till end<br>TC: O(nlogn)<br>SC: O(n) or O(1) depending on sorting algo<br>3. Hashset -> declare seen=set(), for num in nums, if num present in seen, then true else add that num and if complete num doesnt have that number then ret False<br>TC: O(n)<br>SC: O(n)<br>4. Hashset length -> declare return len(set(nums))<len(nums)), set contains unique nos, example nums len = 4 (has 1 dupe), then set = 3 (no dupe) and if matching then True else False<br>TC = O(n)<br>SC = O(n) | [Python](217-contains-duplicate/contains-duplicate.py) |
| 2 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | 🟢 Easy | Array, Two Pointers | 1. Extra Spacing -> declare a temp array and append if num !=0. Declare a for loop and if i<len(tmp) then nums[i]=tmp(i) else nums[i]=0. Example 1,2,3,0,0 and tmp=1,2,3 (first 3 pos are filled for last 2 0's it goes to else condition)<br>TC: O(n)<br>SC: O(n)<br>2. Two Pointer (Two Pass) -> declare l=0 , itr r in range len(nums). Push if nums[r] != 0 and increase l by 1. While loop to cmp l<len(nums) and put nums[l] as 0 and itr till condition false.<br>TC: O(n)<br>SC: O(1)<br>3. Two Pointers (One Pass) -> Do a swap nums[l], nums[r]=nums[r], nums[l]<br>TC: O(n)<br>SC: O(1) | [Python](283-move-zeroes/move-zeroes.py) |
| 3 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 🟢 Easy | Mid Level, Array, Sliding Window | 1. Sum first K elements, slide across array -> add new element Subtract the element leaving window, track max sum seen and divide final max by k to get avg<br>TC: O(n) - Scan array once<br>SC: O(1) - No extra space | [Python](643-maximum-average-subarray-i/maximum-average-subarray-i.py) |
<!-- PROBLEMS:END -->
