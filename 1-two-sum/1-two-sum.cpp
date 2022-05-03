class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int end = nums.size();
        map<int, int> hash;
        for(int i = 0; i < end; i++){
            int goal = target - nums[i];
            if(hash.count(goal) > 0) {
                return {i, hash[goal]};
            }
            hash[nums[i]] = i;
        }
        return {-1,-1};
    }
};