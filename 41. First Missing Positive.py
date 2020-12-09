# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         s = set(nums)
        
#         if len(s) == 0:
#             return 1
#         i = 1
#         for j in range(len(s)):
#             if i not in s:
#                 return i
#             i += 1
#         return i

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        
        if len(s) == 0:
            return 1
        
        i = 1
        while True:
            if i not in s:
                return i
            i += 1