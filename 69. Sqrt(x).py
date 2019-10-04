# 69. Sqrt(x)

'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0: return x
        low = 0
        high = x
        while low <= high:
            mid = (low+high) // 2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans
'''
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x<2: return x;
        
#         low, mid = 0, 0 
#         high = x
        
#         while low<high:
#             mid = low + (high-low)//2
#             if mid > x//mid:
#                 high = mid-1
#             else:
#                 low = mid+1
#                 if low > x//low:
#                     return mid
#         return low
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2: return x
        return int(x**0.5)