class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0] == "0"):
            return 0
        def valid(s: str) -> bool:
            if(s[0] == "0"):
                return False
            # print(s)
            # print(int(s) <= 26 and int(s) >= 1)
            return (int(s) <= 26 and int(s) >= 1)
        length = len(s)
        dp = [0] * length
        for i in range(length):
            if(valid(s[i])):
                dp[i] = dp[i - 1] if i - 1 >= 0 else 1
            if(i - 1 >= 0 and valid(s[i - 1:i + 1])):
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1
        # print(dp)
        return dp[length - 1]