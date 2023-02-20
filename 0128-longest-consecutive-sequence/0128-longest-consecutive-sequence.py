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
            cur_length = 0
            j = num
            while j in nums_set:
                cur_length += 1
                j += 1
            max_length = max(max_length, cur_length)
        return max_length
            