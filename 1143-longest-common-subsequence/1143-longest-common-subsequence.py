class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        t = [[0 for i in range(length2 + 1)] for i in range(length1 + 1)]
        i = 1
        j = 1
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if text1[i-1] == text2[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                else:
                    t[i][j] = max(t[i][j - 1], t[i - 1][j])


        return t[length1][length2]
                
        