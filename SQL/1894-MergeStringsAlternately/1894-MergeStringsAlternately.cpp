// Last updated: 6/27/2026, 8:32:07 PM
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str="";
        int i=0;
        int j=0;
        
        while(i<word1.size() && i<word2.size()){
           str += word1[i];
           str += word2[j];
           i++;
           j++;
        }
        while(i<word1.size()){
            str += word1[i];
            i++;
        }
        while(j<word2.size()){
            str += word2[j];
            j++;
        }
    return str;
    }

};