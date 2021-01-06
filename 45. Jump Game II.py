# 45. Jump Game II
# Greedy policy: always take the largest step it can take and store the position it can reach

class Solution:
    def jump(self, nums: List[int]) -> int:
        last, cur, cnt = 0, 0, 0
        
        for i in range(len(nums)-1):
            cur = max(cur, i+nums[i])
            if i == last:
                last = cur
                cnt += 1
                
        return cnt