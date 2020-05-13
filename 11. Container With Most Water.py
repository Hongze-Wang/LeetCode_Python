# 11. Container With Most Water

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxarea = 0
#         low = 0
#         high = len(height)-1
#         while low < high:
#             maxarea = max(maxarea, min(height[low], height[high]) * (high-low))
#             if height[low] < height[high]:
#                 low += 1
#             else:
#                 high -= 1

#         return maxarea

# it will be faster if you do not use the library func max and min
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        low = 0
        high = len(height)-1
        
        while low < high:
            res = 0
            if height[low] < height[high]:
                res = height[low] * (high-low)
                low += 1
            else:
                res = height[high] * (high-low)
                high -= 1
            if maxarea < res:
                maxarea = res
        
        return maxarea