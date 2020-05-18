# 95. Unique Binary Search Trees II
# G(n) = f(1)+f(2)+...+f(n)
# f(i) = G(i-1) * G(n-i)
# see 96 for more info
# Defintion
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen(low, high):
            return [None] if low == high else [TreeNode(i, l ,r) for i in range(low, high) for l in gen(low, i) for r in gen(i+1, high)]
        return [] if n == 0 else gen(1, n+1)