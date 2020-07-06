# 458. Poor Pigs

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest / minutesToDie
        return math.ceil(math.log(buckest) / math.log(states))
