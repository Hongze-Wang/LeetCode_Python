# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums==None or len(nums)==0: 
            return 0
        max = nums[0]
        for i in range(len(nums)-1):
            if nums[i]>0: 
                nums[i+1] += nums[i]
            if max<nums[i+1]: 
                max = nums[i+1]     
        return max