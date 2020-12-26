# 123. Best Time to Buy and Sell Stock III

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l1, h1, l2, h2 = -float('inf'), 0, -float("inf"), 0
        for p in prices:
            l1 = max(l1, -p)
            h1 = max(h1, l1+p)
            l2 = max(l2, h1-p)
            h2 = max(h2, l2+p)
        return h2