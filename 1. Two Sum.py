# 1. Two Sum

class Solution:
    def twoSum(self, nums, target):
        original_nums = nums[:]
        nums.sort()
        end = len(nums)-1
        start = 0

        while(start < end):
            if nums[start] + nums[end] == target:
                break;
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        
        if nums[start] != nums[end]:
            return [original_nums.index(nums[start]), original_nums.index(nums[end])]
        else:
            new_s = original_nums.index(nums[start])
            new_e = new_s + 1 + original_nums[new_s+1:].index(nums[end])
            return [new_s, new_e]