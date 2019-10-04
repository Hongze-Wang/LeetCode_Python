# 100. Same Tree
# 100% faster 100% less 最直观的递归方法见Java解法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Non
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tmp1, tmp2 = [], []
        
        def inOrder(root, lst):
            if root:
                lst.append(root.val)
                if root.left != None:
                    inOrder(root.left, lst)
                else:
                    lst.append(None)
                
                if root.right != None:
                    inOrder(root.right, lst)
                else:
                    lst.append(None)
                return lst
        res1 = inOrder(p, tmp1)
        res2 = inOrder(q, tmp2)

        return res1 == res2
