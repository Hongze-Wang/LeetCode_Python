# 107. Binary Tree Level Order Traversal II

# 这道题常用解法是BFS 经典的BFS见Java解法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict:

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        dct = defaultdict(list)
        def dfs(depth, node): # 虽然利用字典达到了BFS的效果 但本质是DFS
            dct[depth].append(node.val)
            if node.left:
                dfs(depth+1, node.left)
            if node.right:
                dfs(depth+1, node.right)
        dfs(0, root)
        ans = []
        for key in sorted(dct.keys(), reverse=True)
            ans.append(dct[key])
        return ans
