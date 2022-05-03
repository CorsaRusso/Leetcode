class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int count = 0;
        for(int i = 0; i < nums.size(); i ++){
            if (nums[i] == 0){
                count++;
            }
        }
        if(count > 1){
            for(int i = 0; i < nums.size(); i ++){
                nums[i] = 0;
            }
            return nums;
        } else if (count == 1){
            for(int i = 0; i < nums.size(); i ++){
                if(nums[i] != 0){
                    product *= nums[i];
                }
            }
            for(int i = 0; i < nums.size(); i ++){
                if(nums[i] != 0){
                    nums[i] = 0;
                } else {
                    nums[i] = product;
                }
            }
        } else {
            for(int i = 0; i < nums.size(); i ++){
                product *= nums[i];
            }
            for(int i = 0; i < nums.size(); i ++){
                nums[i] = product / nums[i];
            }
        }
        return nums;
    }
};