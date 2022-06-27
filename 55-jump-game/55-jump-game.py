class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [0] * l
        dp[0] = 1
        for i in range(l):
            if(dp[i] == 1):
                for j in range(nums[i] + 1):
                    dp[i + j] = 1
                    if(dp[l - 1] == 1):
                        return True
        return dp[l - 1]