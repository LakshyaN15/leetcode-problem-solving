# My Solution
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n=len(nums)
#         for i in nums:
#             count=0
#             for j in nums:
#                 if j==i:
#                     count+=1
#                     if count > n//2:
#                         return i

# Alternate Solution
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting
# Input: nums = [3,2,3]
# Output: 3
# Explanantion: 
# Approach: 1. Brute Force -> Using nested loop or count=sum(1 for i in nums if i==num), adds 1 for every element found and > 1 (Time Limit Exceeded)
# TC: O(n^2)
# SC: O(1)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n=len(nums)
#         for num in nums:
#             count=sum(1 for i in nums if i==num)
#             if count>n//2:
#                 return num

# Approach: 2. Hash Map -> declare a defaultdictionary
# TC: O(n)
# SC: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)
        res=maxCount=0

        for num in nums:
            count[num]+=1
            if maxCount < count[num]:
                res=num
                maxCount=count[num]
        return res