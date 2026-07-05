# Topics: Staff, Hash Table, String, Sliding Window
# Input: s = "abcabcbb"
# Output: 3
# Explanantion: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Approach: 1. Sliding Window -> 
# TC:
# SC: 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            charSet=set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res=max(res,len(charSet))
        return res
        