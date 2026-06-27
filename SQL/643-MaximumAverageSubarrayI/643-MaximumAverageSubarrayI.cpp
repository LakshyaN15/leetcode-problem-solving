// Last updated: 6/27/2026, 8:32:20 PM
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {

        int sum=0;
        int n=nums.size();
        for(int i=0; i<k; i++)
        {
            sum += nums[i];
        }
        int maxSum=sum;
        int start=0;
        int end=k;
        while(end<n){
            sum -= nums[start];
            start++;
            sum += nums[end];
            end++;
            maxSum=max(sum,maxSum);
        }

        return (double) maxSum/k;
        
    }
};