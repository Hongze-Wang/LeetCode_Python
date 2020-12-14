# 84. Largest Rectangle in Histogram
# 递增栈
# 每次遇到非递增元素 可以计算一次面积 在所有计算的面积中找到最大的即可
# 巧妙的利用了递增栈的性质

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        heights.append(-1)

        for idx, val in enumerate(heights):
            while heights[stack[-1]] > val:
                h = heights[stack.pop()]
                res = max(res, h*(idx - stack[-1]-1))
            stack.append(idx)
        return res

# Time Limit Exceeded
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights:
#             return 0
#         res = 0
#         for i in range(len(heights)):
#             min_h = heights[i];
#             for j in range(i, len(heights)):
#                 min_h = min(min_h, heights[j])
#                 res = max(res, min_h * (j-i+1))
#         return res
