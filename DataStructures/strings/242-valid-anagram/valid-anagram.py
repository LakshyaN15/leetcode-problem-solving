# Approach: 1. Sorting -> check characters with same freq. Use sorted() to check both strs.
# TC: O(nlogn+mlogM)
# SC: O(1) or O(n+m) depending on sorting algo
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         return sorted(s)==sorted(t) # Sorted() gives list eg, ('a','b','c'...)
        # syntax: sorted(iterable, key=key, reverse=reverse)

# Approach: 2. Hash Map -> Char and freq check, then use countS and countT
#  hash map (or dict) to track freq, if matches both count(key,val) then true
# TC: O(n+m) , n is len of s and m len of t
# SC: O(1) since we have 26 diff char
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         countS,countT={},{}
#         for i in range(len(s)):
#             countS[s[i]]=1+countS.get(s[i],0) # 1 is the default count and get s[i] means if found for 
                                                # that alphabet (key,value) then plus count else 0
                                                # count['a']=1+get(s[i],0), 0 for new and 1 for already in dict
#             countT[t[i]]=1+countT.get(t[i],0) # 1 is the default count and get t[i] means if found for 
                                                # that alphabet (key,value) then plus count else 0
                                                # count['a']=1+get(s[i],0), 0 for new and 1 for already in dict

#             # count.get() is dict key
#         return countS==countT 

# Approach: 3. Hash Table (using arr)-> char and freq check, declare 0-25 arr 
# used ord to convert to ascii char eg, count['b'-'a']=1(98-97), check same for t
# Trick: +1 count for s[i] and -1 for t[i], if present then res will be 0 for all. if val != 0 in end then False else True
# TC: O(n+m)
# SC: O(1) sicne we have 26 diff char
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count=[0]*26 # Declare 0-25 array with all vals 0
        for i in range (len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
        