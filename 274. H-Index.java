# 274. H-Index

class Solution:
    def hIndex(self, c: List[int]) -> int:
        s.sort(reverse=True)
        counter = 0
        for i in range(len(c)):
            if c[i] > counter:
                counter += 1
        return counter
