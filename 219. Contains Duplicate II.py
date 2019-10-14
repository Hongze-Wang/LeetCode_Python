# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums is None or k < 1:
            return False

        if len(list(set(nums))) == len(nums):return False
        
        dic = {}
        for i, v in enumerate(nums):
            if v in dic:
                if i - dic[v] <= k:
                    return True
            dic[v] = i
        return False

# 先判断有没有相同元素 能加速运行
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        
        dic = {}
        for i, v in enumerate(nums):
            if v in dic:
                if i - dic[v] <= k:
                    return True
            dic[v] = i
        return False