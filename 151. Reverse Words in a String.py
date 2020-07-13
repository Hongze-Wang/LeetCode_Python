# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s:str) -> str:
        lis = s.split()
        lis.reverse()
        ans = " ".join(lis)
        return ans
