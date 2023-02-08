class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # dictionary: { frequency: set() }
        # at the start this is filled from 0-n where n is number of elements the array
        # dictionary: { num: frequency }
        # at the start this is empty {}
        # Input: nums = [1,1,1,2,2,3], k = 2
        # Output: [1,2]
        
        frequency = {}
        for i in range(len(nums)):
            frequency[i+1] = set()
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                frequency[nums_dict[i]].remove(i)
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
            frequency[nums_dict[i]].add(i)
        
        retval = []
        for i in range(len(nums)):
            retval += list(frequency[i+1])
            
        return retval[-k:]