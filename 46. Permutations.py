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
