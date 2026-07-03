# Topics: Array, Hash Table, Sorting
# Input: [1,2,3,1]
# Output: true
# Explanantion: The element 1 occurs at the indices 0 and 3.

# Approach: 1. Brute Force -> Declare two var i and j and compare with next, if equal then True else False
# TC: O(n^2)
# SC: O(n)

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False

# Approach: 2. Sorting -> Sort using nums.sort() then compare from idx 1 to prev till end
# TC: O(nlogn)
# SC: O(n) or O(1) depending on sorting algo

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]:
#                 return True
#         return False  

# Approach: 3. Hashset -> declare seen=set(), for num in nums, if num present in seen, then true else add that num and if complete num doesnt have that number then ret False
# TC: O(n)
# SC: O(n)

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen=set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)    
#         return False 

# Approach: 4. Hashset length -> declare return len(set(nums))<len(nums)), set contains unique nos, example nums len = 4 (has 1 dupe), then set = 3 (no dupe) and if matching then True else False
# TC = O(n)
# SC = O(n) 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
