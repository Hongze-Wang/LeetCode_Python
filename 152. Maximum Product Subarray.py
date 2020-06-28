# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = maxp = minp = nums[0]
        for n in nums[1:]:
            maxp, minp = max(maxp*n, minp*n, n), min(maxp*n, minp*n, n)
            ans = max(ans, maxp)
        return ans
