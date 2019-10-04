# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = strs.pop()
        max_len = len(prefix)
        for s in strs:
            while(not(prefix[:max_len] == s[:max_len])):
                max_len -= 1
        return prefix[:max_len]