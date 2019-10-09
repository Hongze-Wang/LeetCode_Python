# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n):
        return len(str(bin(n))[2:].replace('0', ''))

# The result of bin() start with '0b', so the index start from 2

