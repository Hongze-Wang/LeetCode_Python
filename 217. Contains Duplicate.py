# 217. Contains Duplicate

# 最直观的想法 超时
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lis = []
        for i in range(len(nums)):
            if nums[i] in lis:
                return True
            else:
                lis.append(nums[i]);
        return False

# collection.Counter([items]) return a dict key: item - value: numbers of appearance
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) - len(collections.Counter(nums)) > 0

# using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 1:
            return False
        return len(set(sum)) != len(nums)