class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [0] * l
        index = 0
        dp[0] = 1
        for i in range(l):
            if(dp[i] == 1):
                if(i + nums[i] + 1 >= l):
                    return True
                else:
                    for j in range(index - i, nums[i] + 1):
                        print(i , j)
                        dp[i + j] = 1
                index = max(i + nums[i], index)
                # print(index)
                # print(dp)
        # print(dp)
        return dp[l - 1]