# Topics: Array, Prefix Sum
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Explanantion: 
# Approach: 1. Brute Force - declare 2 var i, j and itr them till end. If i==j , continue(skip) , product*=nums[j]. Add to res[i] or res.append. Return res in end
# TC: O(n^2)
# SC: O(1) extra space and O(n) for output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range (len(nums)):
            product=1
            for j in range(len(nums)):
                if j==i: # Not nums[i]==nums[j] as if in diff idx value same example [1,2,1,3] then code will break
                    continue
                product*=nums[j]
            res.append(product)
        return res        
            
# Approach: 2. Prefix and Suffix - declare prefix and suffix as 1 , declare res as [0] * n array, store prefix from right to left in res and suffix after from left to right
# TC: O(n)
# SC: O(1), excluding op array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n

        prefix=1
        for i in range (n):
            res[i]=prefix
            prefix *= nums[i]
        
        suffix=1
        for i in range (n-1,-1,-1):  # (n-1 - from end, -1 = till 0 excluding -1 and -1=step)
            res[i] *= suffix
            suffix *= nums[i]
        return res

