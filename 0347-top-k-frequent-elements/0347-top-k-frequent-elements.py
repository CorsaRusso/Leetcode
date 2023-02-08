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
        
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] +1
            else:
                dic[i] = 1
        
        arr = sorted(dic, key = dic.get,reverse = True)
        return(arr[:k])