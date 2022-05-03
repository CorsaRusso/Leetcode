class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int end = nums.size() - 1;
        int start = 0;
        vector<int> retval = {};
        while(start < end){
            for (int i = start + 1; i <= end; i++){
                if(nums[start] + nums [i] == target){
                    retval = {start,i};
                    return retval;
                }
            }
            start++;
        }
        return retval; 
    }
};