# 205. Isomorphic Strings

# using zip() %98 faster
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

# using mapping 
# 效率超级差 思想可以学习一下
# 将同种元素映射到不同的索引上 保存所有元素的索引作为 字符串模式的一种mapping
# 最后比较两个字符串的mapping是否相等
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def pat(arr, lis, st):
            for s in st:
                if s in lis:
                    arr.append(lis.index(s))
                else:
                    lis.append(s)
                    arr.append(lis.index(s))
            return arr
        pn, ps = [], []
        pn = pat([], [], s)
        ps = pat([], [], t)
        if pn == ps:
            return True
        else:
            return False

# using dict 98% faster
# also the using of mapping idea
# key = elem in s value = elem in t, same index
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            elif t[i] in dic.values(): #和t[i]对应的s[i]字符不同 也是一种不匹配
                return False
            else:
                dic[s[i]] = t[i]
        return True