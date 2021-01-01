# 1363. Largest Multiple of Three

# 维护3个小根堆 第一个堆存除3余0的 第二个堆存除3余1的 第三个堆存除3余2的
# 第二个堆和第三个堆都是删除候选堆 用来不能被3整除时删除一些元素
# 计算数组所有数字的和
# 如果和除3余1 则我们需要去第二个堆删掉堆顶一个元素 如果第二个堆是空的 则需要去第三个堆删除两个元素
# 如果和除3余2 则我们需要去第三个堆删掉堆顶一个元素 如果第三个堆是空的 则需要去第二个堆删除两个元素
# 使用小根堆的特性删除的是最小的数字 同时上面删除元素的规则也保证了只需要删除最小数量的元素
# 两者保证了最后留下来的数字能组成最大的数值
# python解法使用heappush和heappop直接在字典上维护堆
# 最后需要注意“00000”这种特殊情况 所以用了str(int(res))

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = defaultdict(list)
        
        for d in digits:
            heappush(count[d%3], d)
            
        total = sum(digits)
        
        if total % 3 == 1:
            if 1 in count:
                heappop(count[1])
            elif 2 in count:
                heappop(count[2])
                heappop(count[2])
        elif total % 3 == 2:
            if 2 in count:
                heappop(count[2])
            elif 1 in count:
                heappop(count[1])
                heappop(count[1])
        
        res = []
        for lis in count.values():
            res += lis
        
        res = ''.join(map(str, sorted(res, reverse=True)))
        
        return str(int(res)) if res else ""