# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = []
#         for i in nums:
#             if i not in result:
#                 result.append(i)
#             else:
#                 result.remove(i)
#         return result.pop()

# Best
# class Solution:
#     def singleNumber(self, nums):
#         hash_table = {}
#         for i in nums:
#             try:
#                 hash_table.pop(i)
#             except:
#                 hash_table[i] = 1
#         return hash_table.popitem()[0]

# class Solution:
#     def singleNumber(self, nums):
#         return 2*sum(set(nums)) - sum(nums)

# Bit Manipulation
class Solution:
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a