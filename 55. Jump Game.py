# 55. Jump Game

# simple backtracking: Time Limit Exceed
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         def canReach(nums, index):
#             if index == n-1:
#                 return True
#             fur = min(index+nums[index], n-1)
#             for i in range(index+1, fur+1):
#                 if canReach(nums, i):
#                     return True
#             return False
                
#         return canReach(nums, 0)

# optimized Time Limit Exceed
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         def canReach(nums, index):
#             if index == n-1:
#                 return True
#             fur = min(index+nums[index], n-1)
#             for i in range(fur, index, -1):
#                 if canReach(nums, i):
#                     return True
#             return False
                
#         return canReach(nums, 0)

# Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums)-1
        for i in range(lastPos, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
