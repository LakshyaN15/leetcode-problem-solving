// Last updated: 6/27/2026, 8:33:03 PM
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int ind=-1;
        int n=nums.size();
        for(int i=n-2; i>=0; i--){
            if(nums[i]<nums[i+1]){
            ind=i;
            break;
            }
        }
        for(int i=n-1; i>=ind && ind!=-1; i--){
        if(nums[i]>nums[ind]){
            swap(nums[i],nums[ind]);
            break;
        }
                
    }
    reverse(nums.begin()+ind+1, nums.end());
    }
};