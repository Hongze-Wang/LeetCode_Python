# 516. Longest Palindromic Subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]* n for _ in range(n)]

        for l in range(n):
            for i in range(n):
                j = i+l
                if l == 0:
                    dp[i][i] = 1
                else:
                    if j<n and s[i]==s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    elif j<n and s[i]!=s[j]:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
