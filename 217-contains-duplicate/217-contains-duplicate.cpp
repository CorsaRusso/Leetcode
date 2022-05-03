class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> map;
        for(int i = 0; i < nums.size(); i++){
            map[nums[i]] = i;      
        }
        return !(map.size() == nums.size());
        
    }
};