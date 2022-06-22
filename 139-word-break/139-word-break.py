class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = sorted(wordDict, key=len)
        dp = [1] + [0] * len(s)
        for i in range(1, len(s) + 1):
            for j in words:
                if(dp[i - len(j)] == 1 and i - len(j) >= 0 and s[i - len(j):i] == j):
                    dp[i] = 1
                    break
        return dp[len(s)]
        