// Last updated: 6/27/2026, 8:32:31 PM
/* // 1. Brute Force (Nested Loops)
        T.C: O(N^2) ,  Where N is the size of the Array(nums).
        Here Two nested loop creates the time  complexity. 

        S.C: O(1): Constant space. Extra space is 
        only allocated for the Array(output), however the
        output does not count towards the space complexity. */

/***************** Approach 1 *****************/
// class Solution {
// public:
//     vector<int> productExceptSelf(vector<int>& nums) {
//      int n=nums.size();  
//      vector<int>v1;              
   
//      for(int i=0; i<n; i++){
//          int prod=1;
//         for(int j=0; j<n; j++){
//             if(i==j) continue;
//             prod=prod*nums[j];
//         }
//         v1.push_back(prod);
//      }   
//     return v1;
//     }
// };

/*
    2. Better Approach [DP(Tabulation)]
    Time Complexity : O(N), As we iterate the Array(nums) thrice. Where N = size of the array.

    Space complexity : O(N), Array(left_Product and right_Product) space. 

    Solved using Dynamic Programming Approach(tabulation).

*/


/***************** Approach 2 *****************/

// class Solution{
//     public:
//     vector<int> productExceptSelf(vector<int>& nums){
//         int n=nums.size();
//         vector<int> ans(n);
//         vector<int> left_Product(n);
//         vector<int> right_Product(n);
//         left_Product[0] = 1;
//         for(int i=1; i<n; i++){
//             left_Product[i] = left_Product[i-1]*nums[i-1];
//         }

//         right_Product[n-1]=1;
//         for(int i=n-2; i>=0; i--){
//             right_Product[i]=right_Product[i+1]*nums[i+1];
//         }
//         for(int i=0; i<n; i++){
//             ans[i]=right_Product[i]*left_Product[i];
//         }
//         return ans;
//     }
// };

/*
    3. Optimized Approach: DP(Space Optimized)
    Time Complexity : O(N), As we iterate the Array(nums) twice. Where N = size of the array.

    Space complexity : O(1), Constant space. Extra space is only allocated for the Array(output), however the
    output does not count towards the space complexity.

    Solved using Dynamic Programming Approach(Space Optimization). Optimized Approach.

*/

/***************** Approach 3 *****************/

class Solution{
    public:
    vector<int> productExceptSelf(vector<int>& nums){
            int n = nums.size();
        vector<int> output(n);
        output[0] = 1;
        for(int i=1; i<n; i++){
            output[i] = output[i-1] * nums[i-1];
        }
        int right = 1;
        for(int i=n-1; i>=0; i--){
            output[i] *= right;
            right *= nums[i];
        }
        return output;
    }
};