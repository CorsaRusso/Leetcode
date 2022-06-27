class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [0] * l
        dp[0] = 1
        for i in range(l):
            if(dp[i] == 1):
                if(i + nums[i] + 1 >= l):
                    return True
                else:
                    for j in range(nums[i] + 1):
                        dp[i + j] = 1
        print(dp)
        return dp[l - 1]