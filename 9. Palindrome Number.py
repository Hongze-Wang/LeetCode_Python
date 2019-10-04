# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        x_r = int(str(x)[::-1])

        if x != x_r: return False
        else: return True