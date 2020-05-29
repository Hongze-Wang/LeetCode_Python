# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict()
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] >= start:
                    max_len = max(max_len, i - start)
                    start = dic[s[i]] + 1
            dic[s[i]] = i
        return max(max_len, len(s) - start)
