class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_len = len(nums) - 1
        if(dp_len == 0):
            return nums[0]
        dp = [0] * dp_len
        retval = 0
        for i in range(dp_len):
            cur = dp[i - 2] if (i - 2 >= 0) else 0
            prev = dp[i - 1] if (i - 1 >= 0) else 0
            dp[i] = max(cur + nums[i], prev)
            retval = max(retval, dp[i])     
        retval2 = 0
        dp2 = [0] * (dp_len + 1)
        for i in range(1, dp_len + 1):
            cur = dp2[i - 2] if (i - 2 >= 0) else 0
            prev = dp2[i - 1] if (i - 1 >= 0) else 0

            dp2[i] = max(cur + nums[i], prev)
            retval2 = max(retval2, dp2[i])
        return max(retval2, retval)
        