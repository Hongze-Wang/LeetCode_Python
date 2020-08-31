# 72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if i == l1 or j == l2:
                    dp[i][j] = l2 - j if i == l1 else l1 - i
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                    
        return dp[0][0]
