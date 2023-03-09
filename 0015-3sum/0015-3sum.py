class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        retval = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur_three_sum = nums[l] + nums[r] + nums[i]
                if cur_three_sum > 0:
                    r -= 1
                elif cur_three_sum < 0:
                    l += 1
                else:
                    retval.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return retval
        