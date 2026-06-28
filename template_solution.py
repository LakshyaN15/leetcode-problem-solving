"""
Problem: <number>. <Title>
Link:    https://leetcode.com/problems/<slug>/
Pattern: <e.g. Arrays & Hashing>
Difficulty: Easy | Medium | Hard

Approach:
    <one or two lines on the idea>

Time:  O(?)
Space: O(?)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []
