# Title: 1. Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Topics: Math
# TC: O(n)
# SC: O(n)
# Approach: 1. Brute Force - initialize 2 var I and j to itr and check if nums[i]==nums[j] return true return false end;
# TC = O(n^2) SC=O(n)
# 2. Sorting - sort using nums.sort() and compare nums[i]==nums[i-1]
# TC=O(nlogn) SC=O(1) or O(n)
# 3. Hashset = declare a set and initialize another var num, for loop num in nums and if condition, if num is present in seen then true , if not add and in the end return false.
# TC= O(n)
# SC=O(n)

class Solution(object):
    def reverse(self, x: int) -> int:

        s = str(x)
        if s[0] == '-':
            rev = '-' + s[:0:-1]
        else:
            rev = s[::-1]
        
        num = int(rev)
        
        if -2**31 <= num <= 2**31 - 1:
            return num
        return 0
        
