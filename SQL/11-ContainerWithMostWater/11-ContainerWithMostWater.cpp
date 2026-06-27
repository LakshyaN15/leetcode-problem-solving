// Last updated: 6/27/2026, 8:33:13 PM
// BRUTE FORCE 
// TIME COMPLEXITY: O(n^2)
// SPACE COMPLEXITY: O(1)

// class Solution {
// public:
//     int maxArea(vector<int>& height) {
//         int mx=INT_MIN;
      
//         for(int i=0; i<height.size(); i++){
//             for(int j=i+1; j<height.size(); j++){
//                int water=(j-i)*min(height[i],height[j]);
//                 mx=max(water,mx);
//             }
//         }
//         return mx;           
//     }
// };

/* ------ OPTIMAL APPROACH ----------- */
// TIME COMPLEXITY: O(n)
// SPACE COMPLEXITY: O(1)

class Solution {
public:
    int maxArea(vector<int>& height) {
        int mx=INT_MIN;
        int l=0;
        int r=height.size()-1;
        while(l<r){
            int water=(r-l)*min(height[l],height[r]);
            mx=max(mx,water);
            if(height[l]<height[r]){
                l++;
            }
            else {
                r--;
            }
        }           
        return mx;           
    }
};