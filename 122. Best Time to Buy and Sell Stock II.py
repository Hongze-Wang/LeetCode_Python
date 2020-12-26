# 122. Best Time to Buy and Sell Stock II

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         length = len(prices)
#         low, high = prices[0], prices[0]
#         i, res = 0, 0
        
#         while i < length-1:
#             while i < length-1 and prices[i] >= prices[i+1]:
#                 i += 1
#             low = prices[i]
#             while i < length-1 and prices[i] <= prices[i+1]:
#                 i += 1
#             high = prices[i]
#             res += high - low
        
#         return res
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res