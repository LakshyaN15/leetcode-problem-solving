# Topics: Array, Two Pointers
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Explanantion: 
# Approach: 1. Extra Spacing -> declare a temp array and append if num !=0. Declare a for loop and if i<len(tmp) then nums[i]=tmp(i) else nums[i]=0. Example 1,2,3,0,0 and tmp=1,2,3 (first 3 pos are filled for last 2 0's it goes to else condition)
# TC: O(n)
# SC: O(n)

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         temp=[]
#         for num in nums:
#             if num != 0:
#                 temp.append(num)

#         for i in range (len(nums)):
#             if i < len(temp):
#                 nums[i]=temp[i]
#             else:
#                 nums[i]=0

# Approach: 2. Two Pointer (Two Pass) -> declare l=0 , itr r in range len(nums). Push if nums[r] != 0 and increase l by 1. While loop to cmp l<len(nums) and put nums[l] as 0 and itr till condition false.
# TC: O(n)
# SC: O(1)

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l=0
#         for r in range (len(nums)):
#             if nums[r] != 0 :
#                 nums[l]=nums[r]
#                 l+=1

#         while l < len(nums):
#             nums[l]=0
#             l+=1

# Approach: 3. Two Pointers (One Pass) -> Do a swap nums[l], nums[r]=nums[r], nums[l]
# TC: O(n)
# SC: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range (len(nums)):
            if nums[r]:
                nums[l], nums[r]=nums[r], nums[l]
                l+=1