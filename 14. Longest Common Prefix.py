# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = strs.pop()
        max_len = len(prefix)
        for s in strs:
            while(not(prefix[:max_len] == s[:max_len])):
                max_len -= 1
        return prefix[:max_len]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ''
        for x in zip(*strs):  
            if len(set(x)) > 1:
                return prefix
            prefix += x[0]
        return prefix

# *strs把所有字符串用空格连接起来 
# zip()方法把tuple压缩成list 压缩方式：在tuple的每一位置取一个元素 放到一个tuple中
# 因此遍历得到的list 使用set()对当前元素去重 如果长度为1 则是所有字符串的共有元素 加进前缀
# 如果长度不为1 说有差异元素存在了 直接返回

# lis = ["flower", "flow", "flqwe"]
# print(*lis)
# print(zip(*lis))
# print(list(zip(*lis)))

# flower flow flqwe
# <zip object at 0x000001F774F98188>
# [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'q'), ('w', 'w', 'w')]
