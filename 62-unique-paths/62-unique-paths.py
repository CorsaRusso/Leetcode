class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = m + n - 2
        k = n - 1
        return math.floor(math.factorial(r)/(math.factorial(k) * math.factorial(r - k)))