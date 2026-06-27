// Last updated: 6/27/2026, 8:32:47 PM
/*Time complexity:
O(N) + O(N) = O(N), where N is size of array.

Space complexity:
O(1)

Intuition
The Brute force method says we can simply apply 2 loops for calculaing all sub-arrays and finding the max product.

But, the Optizimed way to solve this problem is using Kadane's Algorithm.

Approach
The Approach to this question is exactly same as Kadane's Algo the only differece is, we will be traversing the array from both sides i.e left to right ( lets say the max prod is maxi1 ) and from right to left ( say max prod is maxi2 ), now the final answer will we max of maxi1 and maxi2.

Ques : Why do we have a need to traverse from right to left ??
Ans : lets take an example
arr {-8,5,3,1,6}

// By traversing left to right we have an answer maxi1.
maxi1 = -720 , which is clearly not the max prod value.
*/
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxi=INT_MIN;
        int prod=1;
        int n=nums.size();
        for(int i=0; i<n; i++){
            prod=prod*nums[i];
            maxi=max(maxi,prod);
            if(prod==0) prod=1; 
        }
        prod=1;
        for(int i=n-1; i>=0; i--){
            prod=prod*nums[i];
            maxi=max(maxi,prod);
            if(prod==0) prod=1;
        }
        return maxi;
    }
};