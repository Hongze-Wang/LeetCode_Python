# 70. Climbing Stairs

# class Solution:
#     def climbStairs(self, n):
        
#         a = (1+math.sqrt(5))/2
#         b = (1-math.sqrt(5))/2
        
#         return int((a**(n+1) -b**(n+1))/math.sqrt(5))

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n<=3: 
#             return n
#         nums = [1,2,3]
#         for i in range(3, n):
#             nums.append(nums[i-1] + nums[i-2])
            
#         return nums[n-1]
class Solution:
    def climbStairs(self, n: int) -> int:
        d = dict()
        d[1] = 1
        d[2] = 2
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]