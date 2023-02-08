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
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]