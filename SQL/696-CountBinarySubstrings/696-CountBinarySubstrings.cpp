// Last updated: 6/27/2026, 8:32:19 PM
class Solution {
public:
    int countBinarySubstrings(string s) {
        int c=1, pre=0, res=0;
        for(int i=1; i<s.size(); i++){
            if(s[i]==s[i-1]) c++;
            else{
                res+=min(pre,c);
                pre=c;
                c=1;
            }

        }
        return res+min(c,pre);
    }
};