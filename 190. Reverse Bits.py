class Solution:
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)
    
# key idea
# the ith position move to 31-i after reverse
# initialize ret as 0
# accumulate every bit until there is no more bit

class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power # pick the last bit of n left shift power bit as the reverse operation
            n >>= 1                 # n right shift 1 bit
            power -= 1              # position move to left by 1 step
        return ret
