# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf') # low = prices[0]
        maxProfit = 0
        
        for p in prices:
            if p < low:
                low = p
            maxProfit = max(maxProfit, p-low)
        
        return maxProfit