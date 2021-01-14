# 300. Longest Increasing Subsequence

# dp(i) 表示从0开始到i最长子序列长度
# 它是这么得到的
# 从左向右扫描 遇到比nums[i]小的元素nums[j]表示我们可能能够更新长度 
# 于是比较当前最大长度和历史dp(j)存储的之前计算的最长自序列长度
# 内层循环结束之后即求得到i之前的最大递增子序列长度 +1 得到包括nums[i]在内的最长递增子序列长度

# dp(length-1)并不一定是最大的数 因此dp(length-1)储存的可能并不是结果
# 需要一个额外的变量储存结果
# 因此需要更新dp(i)之后 同时更新结果

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        res, maxLen = 1, 0
        dp = [0] * length
        dp[0] = 1
        
        for i in range(length):
            maxLen = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxLen = max(maxLen, dp[j])
            dp[i] = maxLen + 1
            res = max(res, dp[i])
        
        return res