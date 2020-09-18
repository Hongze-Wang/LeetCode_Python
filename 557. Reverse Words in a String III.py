# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        res = ""
        for item in strs:
            item = item[::-1]
            res += item
            res += " "
            
        return res.strip()
