// Last updated: 6/27/2026, 8:32:28 PM
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n=nums.size();
        if(n==1 || n==0) return;

        int temp;
        int left=0;
        int right=0;

        while(right<n){
            if(nums[right]==0) ++right;
        
        else { 
            temp=nums[left];
            nums[left]=nums[right];
            nums[right]=temp;
            ++right;
            ++left;
        }
    }
    
    }
};