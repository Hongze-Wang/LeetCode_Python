# 416. Partition Equal Subset Sum
# 完全背包变形题

# DP递推式和优化同完全背包 不一样的地方在于操作的是布尔值 因此使用与运算

#
#
# @param nums int整型一维数组
# @return bool布尔型
#
# s = input()
# s = s[1: len(s)-1]
# nums = list(map(int, s.split(',')))

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        if n == 2:
            return nums[0] == nums[1]
        
        total = sum(nums)
        maxN = max(nums)

        if total&1:
            return False

        target = total // 2
        if maxN > total:
            return False

        dp = [[False] * (target+1) for _ in range(n)]
        dp[0][nums[0]] = True
        
        for i in range(1, n):
            cur = nums[i]
            for j in range(1, target+1):
                if j > cur:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-cur]
                else:
                    dp[i][j] = dp[i-1][j]
        return  dp[-1][-1]

# solution = Solution()
# flag = solution.canPartition(nums)
# if flag:
#     print("true")
# else:
#     print("false")