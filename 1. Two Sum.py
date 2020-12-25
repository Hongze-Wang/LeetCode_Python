# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        for i in range(len(nums)):
            if nums[i] in have:
                return [have[nums[i]], i]
            have[target-nums[i]] = i
        return [0, 0]
