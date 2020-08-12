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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def generate(cur, choice):
            if not choice:
                res.append(cur)
            for i, c in enumerate(choice):
                generate(cur+[c], choice[:i] + choice[i+1:])
                
        generate([], nums)
        
        return res
