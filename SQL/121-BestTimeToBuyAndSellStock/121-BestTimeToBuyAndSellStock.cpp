// Last updated: 6/27/2026, 8:32:51 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        int maxprof=0;
        int minprof=INT_MAX;
        for(int i=0; i<n; i++)
        {
        minprof=min(minprof,prices[i]);
        maxprof=max(maxprof,prices[i]-minprof);
        }
        return maxprof;
    }
};