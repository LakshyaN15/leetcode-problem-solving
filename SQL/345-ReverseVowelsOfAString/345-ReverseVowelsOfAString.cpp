// Last updated: 6/27/2026, 8:32:25 PM
class Solution {
public:
    string reverseVowels(string s) {
        int start=0;
        int end=s.size()-1;
        while(start<end){
            if(!isVowel(s[start])) start++;
            if(!isVowel(s[end])) end--;
            if(isVowel(s[start]) && (isVowel(s[end]))) swap(s[start++], s[end--]);
        }
            return s;
        }
        bool isVowel(char x){
            return x=='a' || x=='e' || x=='i' || x=='o' || x=='u' || x=='A' 
            || x=='E' || x=='I' || x=='O' || x=='U';
        }
    
};