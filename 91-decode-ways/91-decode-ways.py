class Solution:
    def valid(self, s: str) -> bool:
            if(s[0] == "0"):
                return False
            return (int(s) <= 26 and int(s) >= 1)
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if(self.valid(s[i])):
                dp[i] = dp[i - 1] if i - 1 >= 0 else 1
            if(i - 1 >= 0 and self.valid(s[i - 1:i + 1])):
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1
        return dp[len(s) - 1]