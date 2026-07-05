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

# Approach: 2. Hash Map -> declare a defaultdict(int) - a special dictionary that auto-creates missing keys with a default value — and for int, that default is 0. This means you can do count[num] += 1 directly, even the very first time you see num, without ever getting a KeyError, delacre maxCount=res=0 and check if maxCount<count[num], if yes then res=num and maxCount=count[num]. Return max appeared num in end as res
# TC: O(n)
# SC: O(n)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count=defaultdict(int)
#         res=maxCount=0
#         for num in nums:
#             count[num]+=1
#             if maxCount < count[num]:
#                 res=num
#                 maxCount=count[num]
#         return res

# Approach: 3. Sorting -> Approach is to sort as after sort majority element will occupy middle pos no matter what.
# TC: O(nlogn)
# SC: O(1) or O(n) depending on sorting algo

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]


# Approach: 4. Booye Moore -> The Boyer-Moore algorithm works by maintaining a candidate and a count. When we see the candidate, we increment the count; otherwise, we decrement it. When the count reaches 0, we pick a new candidate. Since the majority element appears more than half the time, it will survive this elimination process and remain as the final candidate.
# TC: O(n)
# SC: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=count=0
        for num in nums:
            if count==0:
                res=num
            count+=(1 if res==num else -1)
        return res

# Approach: 5. Bit Manipulation -> (will cover later)
# TC: O(n*32)
# SC: O(32)