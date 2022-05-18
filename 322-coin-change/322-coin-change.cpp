class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(amount == 0){
            return 0;
        }
        int a[amount + 1];
        sort(coins.begin(), coins.end());
        for(int i = 0; i <= amount; ++i){
            a[i] = INT_MAX;
            for(int j : coins){
                if(i - j < 0) break;
                else if(i == j){
                    a[i] = 1;
                    break;
                } else {
                    if(a[i-j] == INT_MAX){
                        continue;
                    }
                    a[i] = min(a[i - j] + 1, a[i]);
                }
            }
        }
        //int counter = 0;
        //for(int it : a){
            //cout << counter<< ":" << it << endl;
            //counter++;
        //}
        if (a[amount] == INT_MAX){
            return -1;
        } else {
            return a[amount];
        }
        
    }
};