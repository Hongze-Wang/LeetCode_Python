# 220. Contains Duplicate III

# 直观解法:O(n^2) 超时

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        size = len(nums)
        
        if size < 2 or k < 0 or t < 0: 
            return False
        
        for i in range(size):
            for j in range(1,k+1):
                if j+i < size and abs(nums[j+i] - nums[i]) <= t:
                    return True
        return False

# using zip()

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if t == 0 and len(set(nums)) == len(nums): #这个判断可以加快速度
            return False
        
        n = len(nums)
        
        nums_index = zip(nums, range(n))
        nums_index.sort()
        
        for i in xrange(n):
            j = i + 1
            while j < n and nums_index[j][0] - nums_index[i][0] <= t:
                if abs(nums_index[j][1] - nums_index[i][1]) <= k:
                    return True
                else:
                    j += 1
        
        return False
