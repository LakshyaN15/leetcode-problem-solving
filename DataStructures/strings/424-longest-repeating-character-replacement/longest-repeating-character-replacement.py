# Topics: Junior, Hash Table, String, Sliding Window
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanantion: Replace the one 'A' in the middle with 'B' and form "AABBBBA".The substring "BBBB" has the longest repeating letters, which is 4.There may exists other ways to achieve this answer too.
# Approach: 1. Brute Force -> declare a res, itr i till len (s) , declare count dict and maxf, itr j from i till len(s) , check if count[s[j]] is present in dict if not then 0 default and add 1 (1+count.get(s[j],0)), take max of maxf or count. Check with if condition whether (j-i+1)-maxf<=k, if yes then max of res or (j-i+1) and return res
# TC: O(n^2)
# SC: O(m), Where n is the length of the string and m is the total number of unique characters in the string.

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         res=0
#         for i in range(len(s)):
#             count,maxf={},0
#             for j in range(i,len(s)):
#                 count[s[j]]=1+count.get(s[j],0)
#                 maxf=max(maxf,count[s[j]])
#                 if (j-i+1)-maxf <= k:
#                     res=max(res,(j-i+1))
#         return res

# Approach: 2. Sliding Window -> 
# TC:
# SC:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        charSet=set(s)

        for c in charSet:
            count=l=0
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                while(r-l+1)-count > k:
                    if s[l]==c:
                        count-=1
                    l+=1
                res=max(res,r-l+1)
        return res
