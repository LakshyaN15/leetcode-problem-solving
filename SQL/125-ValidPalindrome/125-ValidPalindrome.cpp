// Last updated: 6/27/2026, 8:32:50 PM
/*Approach 1. Two Pointer
T.C: O(n): first loop iterates from 0 to n-1, and in second loop it is o(n/2)=O(n) as it starts from start and end and gets finished midway. Hence, O(|s|), where n=size of string or |s|.

S.C: The space complexity of the function is O(1) since the additional space used is constant and does not depend on the size of the input string.

*/

/***************** Approach 1 *****************/

// class Solution {
// public:
//     bool isPalindrome(string s) {
//         int i=0,j=0;
//         int size=s.size();
//         while(j<size){
//             if(s[j]>='A' && s[j]<='Z'){
//                 s[j]=s[j] - 'A' + 'a';
//             }
//             if((s[j]>='a' && s[j]<='z') || (s[j]>='0' && s[j]<='9'))
//             s[i++]=s[j++];
//         }
//         int start=0, end=size-1;
//         while(start<=end){
//             if(s[start]!=s[end]) return false;
//             start++,end--;
//         }
//     return true;
//     }
// };





/* T.C: O(n), n is the size of string and each functions check the condition due to while loop

S.C:O(1), as only constant space is used.

Intuition
By reading the question you may think that first we need to convert the string to desired form and then check if its a valid palindrome or not.

But all of that is just distraction you can check valid palindrome by simply using two pointers no need to convert.

Approach
If a character is not alphanumeric we can simply ignore it and update our pointer to next character (for both pointers)

and then we check by converting the alphanumeric character to lowercase (tolower() function on numbers has no change)
if those two are not equal then return false(not palindrome)
else update both pointers and continue.

Finally after all checking if reach at last then string must be a valid palindrome so return true.

 */
/***************** Approach 2 (BEST APPROACH) *****************/
class Solution{
    public:
    bool isPalindrome(string s){
        int end=s.size()-1;
        int start=0;
        while(start<=end){
            if(!isalnum(s[start])) {start++; continue;}
            if(!isalnum(s[end])) {end--; continue;}
            if(tolower(s[start])!=tolower(s[end])) return false;
        else{
            start++;
            end--;
        }
        
        }
        return true;
    }
};

/* Method 3: using auxiliary data structure
        Time complexity: O(n), space complexity: O(n)
        Not efficient enough */
/***************** Approach 3 *****************/

// class Solution{
// public:
// bool isPalindrome(string s){
//     if(s.empty()) return true;
//     vector<int>v;
//     for(auto ch:s){
//         if(isalnum(ch)){
//             v.push_back(tolower(ch));
//         }
//     }
//                int begin = 0;
//         int end = v.size() - 1;
//         while (begin < end){
//             if(v[begin] != v[end]){
//                 return false;
//             }
//             begin++;
//             end--;
//         }
//         return true;
//         }
// };