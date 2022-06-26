class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0]*l
        for i in range(l):
            cur = dp[i - 2] if i - 2 >= 0 else 0
            prev = dp[i - 1] if i - 1 >= 0 else 0
            dp[i] = max(nums[i] + cur, prev)
        return dp[l-1]
        