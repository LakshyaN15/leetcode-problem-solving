// Last updated: 6/27/2026, 8:33:06 PM
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n=nums.size();
        int j=0;
        for(int i=1; i<n; i++){
            if(nums[i]!=nums[i-1]){
                nums[j+1]=nums[i];
                j++;
            }
        }
        return j+1;
    }
};

// using extra space
// map<int,int> mpp ;
//     for(int i=0;i<nums.size();i++){
//         mpp[nums[i]]++;
//     }  
//     int i=0;
//     for(map<int,int>::iterator it= mpp.begin(); it!=mpp.end();it++){
//         int a=it->first;
//         nums[i]=a;
//         i++;
//     }
//      return i;