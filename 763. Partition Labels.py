# 763. Partition Labels

#  two pointers + greedy
#  greedy policy: partition include one char last appearance

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        start = end = 0
        ans = []
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                ans.append(i-start+1)
                start = i+1
        return ans
