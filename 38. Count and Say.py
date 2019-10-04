# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for i in range(1, n):
            say = 0
            newRes = ""
            toCount = res[0]

            for j in res:
                if j == toCount:
                    say += 1
                else:
                    newRes += str(say) + toCount
                    toCount = j
                    say = 1
            
            newRes += str(say) + toCount
            res = newRes

        return res