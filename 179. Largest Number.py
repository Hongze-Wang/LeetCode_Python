# 179. Largest Number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lis = []
        for i in range(len(nums)):
            lis.append(str(nums[i]))
        
        lis = sorted(lis, key=cmp_to_key(lambda a, b: 1 if b+a > a+b else -1))
        
        res = "".join(lis)
        return "0" if res[0] == "0" else res

class Cmp(str):
    def __lt__(x, y): # 函数名不可更改
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = "".join(sorted(map(str, nums), key=Cmp))
        return "0" if res[0] == "0" else res
