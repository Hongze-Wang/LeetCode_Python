# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def toBST(nums, left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            
            mid = left + (right-left) // 2
            root = TreeNode(nums[mid])
            root.left = toBST(nums, left, mid-1)
            root.right = toBST(nums, mid+1, right)
            
            return root
            
        return toBST(nums, 0, len(nums)-1)