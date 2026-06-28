// TC: O(log base 10 n) as we are 
//using while loop and dividing by 10 at each step
// SC: O(1), as memory is not growing, we arent using arrays , 
// recursion or strings.
class Solution {
public:
    int reverse(int x) {
        int rev=0;
        int digit;
        int max=INT_MAX/10;
        int min=INT_MIN/10;
        while(x!=0)
        {
            digit=x%10;
            if(rev>max || rev<min)
            {
                return 0;
            }
            rev=rev*10+digit;
            x/=10;
        }
    return rev;
    }
};

