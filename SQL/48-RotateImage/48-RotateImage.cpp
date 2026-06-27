// Last updated: 6/27/2026, 8:32:59 PM
// class Solution {
// public:
//     void rotate(vector<vector<int>>& matrix) {
//         int r,c,k=2,t,i=0,j=0;
   
// vector< vector<int> >::iterator row;
// vector<int>::iterator col;
// for (row = matrix.begin(); row != matrix.end(); row++) {
//     j=0;
//     for (col = row->begin(); col != row->end(); col++) {
        
//         t=matrix[i][j];
//         matrix[i][j]=matrix[j][k];
//         matrix[j][k]=t;
//         j++;
//         // do stuff ...
//     }
//     i++;
//     k--;
// }
        
        
//     }    
    
//};

class Solution {
public:
    void rotate(vector<vector<int>>& matrix){
        int i,j;
        int n=matrix.size();
        int m= matrix[i].size();
        
        for( i=0; i<n; i++)
        {
            for( j=0; j<i; j++)
            {
                swap(matrix[j][i], matrix[i][j]);
            }
        }
for( i=0; i<n; i++)
        
            {   
                reverse(matrix[i].begin(), matrix[i].end());
            
        }
}
        
     
    };
            
            
        
    
    