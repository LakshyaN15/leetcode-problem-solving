// Last updated: 6/27/2026, 8:33:23 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      //  vector<int>ans;
      //  sort(nums.begin(),nums.end());
    //     int i,j;
    //     for(i=0; i<nums.size(); i++)
    //     {
    //         for(j=i+1; j<nums.size(); j++)
    //         {
    //             if(nums[i]+nums[j]==target)
    //             return {i,j};
    //         }
    //     }
    //  return {}; 
    // }

    unordered_map<int,int>mp;

    for(int i=0; i<nums.size();i++)
    {
        if(mp.find(target-nums[i])==mp.end())
            mp[nums[i]]=i;
    
    else return {mp[target-nums[i]],i};
    }
    return{-1,-1};
    }
};