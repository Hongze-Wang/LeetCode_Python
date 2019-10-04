# 35. Search Insert Position

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         i=0
#         for index in range(len(nums)):
#             if nums[index] < target:
#                 i += 1
#             else:
#                 break
#         return i
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         return next(filter(lambda x: x[1] >= target, enumerate(nums)), (len(nums), 0))[0]

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]: 
            return 0 # low border case
        if target>nums[-1]: 
            return len(nums) #high border case
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low + (high-low) // 2
            if target==nums[mid]: 
                return mid
            elif target>nums[mid-1] and target<nums[mid]: 
                return mid
            elif target>nums[mid]: 
                low = mid+1
            else: 
                high = mid-1