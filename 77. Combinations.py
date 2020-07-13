# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.combinehelper(range(1, n+1), k, 0, [], res)
        return res
        
    def combinehelper(self, nums, k, index, path, res):
        if k==0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.combinehelper(nums, k-1, i+1, path+[nums[i]], res)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(path, index):
            if len(path) == k:
                res.append(path)
            for i in range(index, n+1):
                dfs(path+[i], i+1)
        dfs([], 1)
        return res
