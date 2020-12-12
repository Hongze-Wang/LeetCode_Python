# 84. Largest Rectangle in Histogram
# 递增栈解法基于一个假设 最大面积一定在一个递增序列上得到
# 这是一种贪心的思想 贪心能取得最优解的原因是 贪心解是唯一解
# 因为只有递增序列能增大面积 贪心策略是唯一的策略 自然也是最优策略

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
