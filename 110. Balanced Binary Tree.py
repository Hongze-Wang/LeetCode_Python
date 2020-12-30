# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.getHeight(root) < 0:
            return False
        else:
            return True

    def getHeight(self, node):
        if node is None:
            return 0
        hl = self.getHeight(node.left)
        hr = self.getHeight(node.right)

        if hl == -1 or hr == -1:
              return -1
        if abs(hl-hr) > 1:
            return -1
        return max(hl, hr) + 1

class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else: return self.isBalanced(root.left) and self.isBalanced(root.right)