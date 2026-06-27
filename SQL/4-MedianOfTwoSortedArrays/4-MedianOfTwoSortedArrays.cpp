// Last updated: 6/27/2026, 8:33:19 PM
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
     vector<int>nums3;
     int n1=nums1.size();
     int n2=nums2.size();
     int i=0, j=0;
     for(i=0; i<n1; i++){
        nums3.push_back(nums1[i]);
     }
     for(j=0; j<n2; j++){
        nums3.push_back(nums2[j]);
     }
     sort(nums3.begin(), nums3.end());
    
    int n=nums3.size();
    return n%2?nums3[n/2]:(nums3[n/2-1]+nums3[n/2])/2.0;
    }
};