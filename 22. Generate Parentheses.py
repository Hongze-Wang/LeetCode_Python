# 22. Generate Parentheses
# Brute Force
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n==0: return ['']
#         ans = []
#         for c in range(n):
#             for left in self.generateParenthesis(c):
#                 for right in self.generateParenthesis(n-1-c):
#                     ans.append('({}){}'.format(left, right))
#         return ans

# standard solution: backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0: 
            return ['']
        
        res = []
        def backtrack(cur, left, right):
            if len(cur) == n*2:
                res.append(cur)
            if left < n:
                backtrack(cur+'(', left+1, right)
            if left > right:
                backtrack(cur+')', left, right+1)
        
        backtrack("", 0, 0)
        
        return res
