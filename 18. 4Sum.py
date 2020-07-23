# 18. 4Sum
# turn into a two sum question and solve it
from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        seen = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i):
                have = nums[i] + nums[j]
                need = target - have
                if need in seen:
                    for k,t in seen[need]:
                        if len({k,t,i,j}) == 4:
                            res.add(tuple(sorted([nums[k], nums[t], nums[i], nums[j]])))
                seen[have].append((i, j))  # avoid collision & this why we should judge the len before add into res
        return res
