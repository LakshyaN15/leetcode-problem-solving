// Last updated: 6/27/2026, 8:32:21 PM
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
       if(n==0) return true;
        for(int i=0; i<flowerbed.size(); i++){
            if(flowerbed[i]==0){
                int next=(i==flowerbed.size()-1)?0:flowerbed[i+1];
                int prev=(i==0)?0:flowerbed[i-1];
                if(next==0 && prev==0){
                  flowerbed[i]=1;
                  n--;
                  if(n==0) {return true;}
                }
            }
        }
        return false;
    }
};