# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone =  {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        res = []
        
        def combinate(cur, remDigits):
            if not remDigits:
                res.append(cur)
                return
            else:
                for char in phone[remDigits[0]]:
                    combinate(cur+char, remDigits[1:])
        
        combinate("", digits)
        return res
