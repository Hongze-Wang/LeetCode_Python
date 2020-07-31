# 20. Valid Parentheses

class Solution:
    def isValid(self, s:str) -> bool:
        stack,match = [], {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in match:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack

# class Solution(object):
#     def isValid(self, s):
#         while "()" in s or "{}" in s or '[]' in s:
#             s = s.replace("()", "").replace('{}', "").replace('[]', "")
#         return s == ''

# class Solution:
#     def isValid(self, s):
#         bracketMap = {"(": ")", "[": "]", "{": "}"}
#         # openBracket = set(["(", "[", "{"])
#         openBracket = ["(", "[", "{"]
#         stack = []
#         for i in s:
#             if i in openBracket:
#                 stack.append(i)
#             elif stack and i == bracketMap[stack[-1]]:
#                 stack.pop()
#             else:
#                 return False
#         return stack == []
