class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = []
        for x in nums:
            if not a or x > a[-1]:
                a.append(x)
            else:
                a[bisect.bisect_left(a, x)] = x 
        return len(a)
        