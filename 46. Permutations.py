# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def generate(cur, choices):
            if not choices:
                ans.append(cur)
                return
            for idx, c in enumerate(choices):
                generate(cur+[choices[idx]], choices[:idx]+choices[idx+1:])
        generate([], nums)
        return ans

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
