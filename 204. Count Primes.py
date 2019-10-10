# 204. Count Primes

# 其实是暴力法 O(n^2)
# 对于每个i从 2i,3i,4i...n都不是质数 因此标定它们不是指数
# 初始化整个数组为全1 将不是质数的标0 最后使用sum函数求和

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        a = [1] * n
        a[0] = 0
        a[1] = 0
        
        for i in range(2, int(n**(.5) + 1)):
            for j in range(i+i, n, i):
                a[j] = 0

        return sum(a)

# 我是第一次知道 LeetCode能导入numpy的
import numpy as np
class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        isPrime = np.ones(n, dtype = bool)
        for i in range(2, int(n**.5) + 1):
            if isPrime[i]:
                isPrime[i**2: n: i] = False #np对象可迭代 因为能切片
        return int(np.sum(isPrime[2:]))

# 结合上述两个的方法
class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n**0.5)+1):
            if s[i] == 1:
                s[i*i: n: i] = [0] * len(s[i*i: n: i])
        return sum(s)