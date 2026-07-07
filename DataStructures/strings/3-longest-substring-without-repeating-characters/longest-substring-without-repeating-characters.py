# Topics: Staff, Hash Table, String, Sliding Window
# Input: s = "abcabcbb"
# Output: 3
# Explanantion: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Approach: 1. Brute Force -> declare i,j and iterate i till len(s) and j from 1 to len(s) , if s[j] in charset break, add to charset and res = max(res,len(charset)) then return res
# TC: O(n^2)
# SC: O(m), M is the size of the character set (e.g., 128 for ASCII). Since M is a fixed number, the space complexity for all approaches can be considered O(1).
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res=0
#         for i in range(len(s)):
#             charSet=set()
#             for j in range(i, len(s)):
#                 if s[j] in charSet:
#                     break
#                 charSet.add(s[j])
#             res=max(res,len(charSet))
#         return res

# Approach: Sliding Window -> We declare a set() , a starting point l , res = 0     Give for loop and while s[r] in charset, if yes, charset.remove(s[r]) and l+=1, else add to charset and use res=max(res,l-r+1), then return res
# TC: O(n)
# SC: O(m), M is the size of the character set (e.g., 128 for ASCII). Since M is a fixed number, the space complexity for all approaches can be considered O(1).

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res


# Approach: 3. Sliding Window (Optimized) -> This is a clever optimization of the sliding window. Instead of slowly shrinking the window one element at a time, we can jump the left pointer directly to the correct position.
# TC: O(n)
# SC: O(m), M is the size of the character set (e.g., 128 for ASCII). Since M is a fixed number, the space complexity for all approaches can be considered O(1).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen={}
        start=0
        res=0

        for end,char in enumerate(s):
            if char in last_seen and last_seen[char]>=start:
                start=last_seen[char]+1
            res=max(res,end-start+1)
            last_seen[char]=end
        return res
