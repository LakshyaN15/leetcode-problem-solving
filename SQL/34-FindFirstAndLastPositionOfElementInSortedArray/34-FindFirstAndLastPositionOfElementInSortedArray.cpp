// Last updated: 6/27/2026, 8:33:01 PM
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n=nums.size();
       int spos=-1;
       int endpos=-1;

        for(int i=0; i<n; i++){
            if(nums[i]==target){
                spos=i;
                break;
            }
        }

        for(int i=n-1; i>=0; i--){
            if(nums[i]==target){
                endpos=i;
                break;
            }
        }
        return {spos, endpos};
    }
};