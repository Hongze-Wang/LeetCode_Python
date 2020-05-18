# 62. Unique Paths
# DP的关键在于递推式
# num(i, j) = num(i-1, j) + num(i, j-1)
# 直观理解即为 到达某格子的单一路径数 = 到达上方格子的路径数 + 到达左方格子的路径数
# 因为之能向左 或 向下移动
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for i in range(n)] for j in range(m)]

        for i in range(n):
            arr[0][i] = 1
        for i in range(m):
            arr[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
        return arr[m-1][n-1]