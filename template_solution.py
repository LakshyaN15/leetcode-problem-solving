# Topics: 
# Input: 
# Output: 
# Explanation: 
# Approach: Eg. 1. Sum first K elements, slide across array -> add new element
# Subtract the element leaving window, track max sum seen and divide final max by k to get avg
# TC: 
# SC: 

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []
