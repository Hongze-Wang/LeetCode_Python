# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashTable = dict()
        for i in set(s):
            hashTable[i] = s.count(i)
            if i not in t or hashTable[i] != t.count(i):
                return False
        return True

# Optimized from the above
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if i not in t or s.count(i) != t.count(i):
                return False
        return True
