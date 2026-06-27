// Last updated: 6/27/2026, 8:32:40 PM
// TIME COMPLEXITY: O(logn), the number of iterations required 
// to reduce n to zero is proportional to the number of bits in n, 
// which is log n
// SPACE COMPLEXITY: O(1)

class Solution {
public:
    int hammingWeight(uint32_t n) {
       int count=0;
       while(n!=0){
           if(n & 1) count++;
           n=n>>1;
       }
       return count;
    }
};