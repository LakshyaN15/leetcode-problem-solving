// Last updated: 6/27/2026, 8:32:45 PM
class Solution {
public:
    int findMin(vector<int>& nums) {
          
           int min1=INT_MAX;
           for(int i=0; i<nums.size(); i++)
           {    
               min1=min(nums[i],min1);
              
           } 
           return min1;
    }
};

