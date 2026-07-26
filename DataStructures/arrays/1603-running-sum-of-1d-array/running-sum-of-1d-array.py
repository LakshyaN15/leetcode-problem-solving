# Approach: 1. Prefix Sum -> Use a Prefix Sum (Running Sum) approach. Maintain a variable `curr_sum` that stores the cumulative sum seen so far. Traverse the array once, add each element to `curr_sum`, and append it to the result list.
# TC: O(n)
# SC: O(n), extra space for storing list
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         result=[]
#         curr_sum=0
#         for num in nums:
#             curr_sum+=num
#             result.append(curr_sum)
#         return result

# Approach: 2. In-Place Prefix Sum -> Traverse the array from the second element and add the previous cumulative sum to the current element. This updates each element to represent the running sum without using any extra array.
# TC: O(n)
# SC: O(1), since input array is modified in place, hence auxilary space
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,(len(nums))):
            nums[i]+=nums[i-1]
        return nums
