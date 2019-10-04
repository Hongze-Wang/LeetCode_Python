from operator import itemgetter
import collections
class Solution:
    def singleNumber(self, nums):
        counter = collections.Counter(nums)
        res = sorted(counter.items(), key=itemgetter(1))
        return res[0][0]