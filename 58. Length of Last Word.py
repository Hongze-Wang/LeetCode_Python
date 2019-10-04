# 58. Length of Last Word

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         if s==None or len(s)==0: 
#             return 0
#         nums = s.split(" ")
#         while ' ' in nums:
#             nums.remove(' ')
#         while '' in nums:
#             nums.remove('')
#         if len(nums)==0: return 0
#         return len(nums[-1])

class Solution:
    def lengthOfLastWord(self, s):
        if not s.split():
            return 0
        return len(s.split()[-1])