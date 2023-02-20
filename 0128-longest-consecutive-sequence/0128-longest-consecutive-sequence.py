class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            now = num
            cur_length = 1
            while(now + 1 in nums_set):
                now += 1
                cur_length += 1
            max_length = max(max_length, cur_length)
        return max_length
            