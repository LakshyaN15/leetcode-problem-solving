// Last updated: 6/27/2026, 8:33:05 PM
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size()>haystack.size()) return -1;
    int s1=haystack.size();
    int s2=needle.size();
    for(int i=0; i<=s1-s2; i++){
        string s=haystack.substr(i,s2);
        if(s==needle) return i;
    }
    return -1;
        
    }
};