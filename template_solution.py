# Title: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topics: Array, Hash Table
# TC: O(n)
# SC: O(n)
#
# Approach: hash map from value -> index; for each number check if its
# complement was already seen.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []
