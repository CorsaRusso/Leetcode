class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        viewed = {}
        for i, j in enumerate(nums):
            if (target - j) in viewed:
                return [i, viewed[target - j]]
            else:
                viewed[j] = i