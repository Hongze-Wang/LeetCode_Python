# 322. Coin Change

# 找零问题 DP
# 在取最小值的场景下 一定要把dp数组初始化到一个不能取得的大数float('inf')
# 取最大值场景 因为默认初始化为0，则没有这个问题

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        return dp[amount] if dp[amount] < amount+1 else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c]+1)
                    
        return dp[amount] if dp[amount] < amount+1 else -1
