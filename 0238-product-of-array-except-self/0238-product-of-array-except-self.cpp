class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int left = 1;
        int right = 1;
        vector<int> vect(n, 1);


        for (int i = 0; i < n; i++){
            int num = n - i - 1;
            vect[i] *= left;
            vect[num] *= right;
            left *= nums[i];
            right *= nums[num];
        }
        return vect;
    }
};