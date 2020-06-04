# 102. Binary Tree Level Order Traversal

# iterative method using DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res, stack = [], [(root, 0)]
        while len(stack) != 0:
            (node, level) = stack.pop()
            if len(res) < level + 1:
                res.append([node.val])
            else:
                res[level].append(node.val)
            if node.right: # visit right first because you are using a stack
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
        return res
