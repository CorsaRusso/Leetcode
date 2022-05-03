class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int left = 1;
        int right = 1;
        vector<int> vect(n, 1);


        for (int i = 0; i < n; i++){
            vect[i] *= left;
            vect[n - i - 1] *= right;
            left *= nums[i];
            right *= nums[n- i - 1];
        }
        return vect;
    }
};