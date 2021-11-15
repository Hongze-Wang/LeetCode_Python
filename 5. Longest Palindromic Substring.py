# plain
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        start = 0
        for i in range(len(s)):
            left = i
            right = i
            while right + 1 < len(s) and s[right+1] == s[left]:
                right += 1
            i = max(i, right)
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if res < right-left-1:
                start = left+1
                res = right-left-1
                
        return s[start:start+res]


# optimized
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        start = 0
        i = 0
        while i < len(s):
            left = i
            right = i
            while right + 1 < len(s) and s[right+1] == s[left]:
                    right += 1
            i = max(i+1, right)
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if res < right-left-1:
                start = left+1
                res = right-left-1
                
        return s[start:start+res]

# optimized
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        start = 0
        i = 0
        while i < len(s):
            left, right = i, i
            while right+1 < len(s) and s[right+1] == s[left]:
                right += 1
            i = max(i+1, right)
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if res < right - left - 1:
                res = right - left - 1
                start = left+1
                
        return s[start: start+res]
