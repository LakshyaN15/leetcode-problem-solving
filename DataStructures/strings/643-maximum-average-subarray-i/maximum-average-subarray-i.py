# Topics: Mid Level, Array, Sliding Window
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Approach: 1. Sum first K elements, slide across array -> add new element
# Subtract the element leaving window, track max sum seen and divide final max by k to get avg
# TC: O(n) - Scan array once 
# SC: (1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k]) # 1+12+(-5),+(-6)=2
        m=s
        for i in range(k,len(nums)):
            s+=nums[i] - nums[i-k] # 2 + nums[4] - nums[4-4=0] = 2+50-1=51
            if s>m:
                m=s
        return float(m)/k