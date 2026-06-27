// Last updated: 6/27/2026, 8:32:38 PM
class Solution { 
    private:
    int nextNumber(int n){
     int digit;
      int sq=0;
      while(n>0){
          digit = n%10;
          sq=sq+(digit*digit);
          n /= 10;
      } 
     return sq;
    }   
        
public:
    bool isHappy(int n) {
        unordered_set<int> set;
        while(n!=1 && !set.count(n)){
            set.insert(n);
            n=nextNumber(n);
        }
        return n==1;
    }
};