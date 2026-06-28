# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:
#         window_sum = sum(nums[:k])
#         max_sum = window_sum
        
#         for i in range(k, len(nums)):
#             window_sum = window_sum - nums[i - k] + nums[i]
#             max_sum = max(max_sum, window_sum)
        
#         return max_sum / k

class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])
        m = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s > m:
                m = s
        return m / float(k)