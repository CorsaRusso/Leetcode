class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longestConsecutive = 0
        for num in numSet:
            length = 0
            if num - 1 not in numSet:
                while num + length in numSet:
                    length += 1
                longestConsecutive = max(length, longestConsecutive)
        return longestConsecutive
            