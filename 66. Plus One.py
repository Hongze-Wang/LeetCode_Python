# 66. Plus One

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = 0
#         result = []
#         if len(digits)==1: num = digits[0] + 1
#         else:
#             for i in range(len(digits)):
#                 num = num*10 + digits[i]
#             num += 1
        
#         snum = str(num)
        
#         for i in range(len(snum)):
#             result.append(int(snum[i]))

#         return result
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(dig) for dig in list(str(int(''.join([str(digit) for digit in digits]))+1))]