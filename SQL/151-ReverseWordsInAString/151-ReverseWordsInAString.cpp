// Last updated: 6/27/2026, 8:32:48 PM
class Solution {
public:
    string reverseWords(string s) {
        //T.C = O(n)
        // S.C = O(n)
        int n=s.size();
        int i=0;
        string str="";
        while(i<n){
            string temp="";
            while(s[i]== ' ' && i<n){
                i++;
            }
            while(s[i]!= ' ' && i<n){
                temp+=s[i];
                i++;
            }
            if(temp.size()>0){
                if(str.size()==0)
                    str=temp;
                
                else 
                    str=temp+" "+str;
                }
            }
        
        return str;
    }
};

