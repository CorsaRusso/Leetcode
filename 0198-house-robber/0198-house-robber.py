class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,2,3,5]
        # [0,0,0,0]
        max_money = [0 for i in nums]
        for i in range(len(max_money)):
            prev_house = 0 if (i - 1) < 0 else max_money[i-1]
            second_prev_house = 0 if (i - 2) < 0  else max_money[i-2]
            max_money[i] = max(prev_house, second_prev_house + nums[i])
        return max_money[-1]
            