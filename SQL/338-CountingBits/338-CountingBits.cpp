// Last updated: 6/27/2026, 8:32:27 PM
class Solution {
public:
    vector<int> countBits(int n) {
       //T.C=O(nlognn), n as another vector arr is created and logn as 
       //number is repetedly getting div by 2 to make it zero
       //S.C=O(n)
        vector<int>ans;
        for(int i=0; i<=n; i++){
            int sum=0;
            int num=i;
            while(num!=0){
                sum += num%2;
                num /= 2;
            }
            ans.push_back(sum);
        }
        return ans;
    }
};