# Strings

**LeetCode tags covered here:** String, String Matching, Rolling Hash, Suffix Array

Solutions in this bucket:

<!-- - [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/) — Easy -->

<!-- PROBLEMS:START -->
| # | Problem | Difficulty | Topics | Approach | Solution |
|---|---------|:----------:|--------|----------|:--------:|
| 1 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟢 Easy | — | 1. Sorting -> check characters with same freq. Use sorted() to check both strs.<br>TC: O(nlogn+mlogM)<br>SC: O(1) or O(n+m) depending on sorting algo class Solution: def isAnagram(self, s: str, t: str) -> bool: if len(s)!=len(t): return False return sorted(s)==sorted(t) # Sorted() gives list eg, ('a','b','c'...) syntax: sorted(iterable, key=key, reverse=reverse)<br>2. Hash Map -> Char and freq check, then use countS and countT hash map (or dict) to track freq, if matches both count(key,val) then true<br>TC: O(n+m) , n is len of s and m len of t<br>SC: O(1) since we have 26 diff char class Solution: def isAnagram(self, s: str, t: str) -> bool: if len(s)!=len(t): return False countS,countT={},{} for i in range(len(s)): countS[s[i]]=1+countS.get(s[i],0) # 1 is the default count and get s[i] means if found for that alphabet (key,value) then plus count else 0 count['a']=1+get(s[i],0), 0 for new and 1 for already in dict countT[t[i]]=1+countT.get(t[i],0) # 1 is the default count and get t[i] means if found for that alphabet (key,value) then plus count else 0 count['a']=1+get(s[i],0), 0 for new and 1 for already in dict<br>3. Hash Table (using arr)-> char and freq check, declare 0-25 arr used ord to convert to ascii char eg, count['b'-'a']=1(98-97), check same for t Trick: +1 count for s[i] and -1 for t[i], if present then res will be 0 for all. if val != 0 in end then False else True<br>TC: O(n+m)<br>SC: O(1) sicne we have 26 diff char | [Python](242-valid-anagram/valid-anagram.py) |
<!-- PROBLEMS:END -->
