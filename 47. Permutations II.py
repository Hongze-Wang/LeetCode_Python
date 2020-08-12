# 47. Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)

        def dfs(cur):
            res = []
            if not counter:
                return [cur]
            for num in list(counter.keys()):
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
                res += dfs(cur + [num])
                counter[num] = counter.get(num, 0) + 1
            return res
        
        return dfs([])
