class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int p = 0;
        int profit = 0;
        for(int i = 0; i < prices.size(); i++){
            profit = max(profit, prices[i] - prices[p]);
            if(prices[i] < prices[p]){
                p = i;
            }
        }
        return profit;
    }
};