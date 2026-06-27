// Last updated: 6/27/2026, 8:33:02 PM
class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i]==target) return i;

        }
        return -1;
    }
};