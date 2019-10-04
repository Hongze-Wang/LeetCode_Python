# Python 2 记录最小值
class ListNode:
    def __init__(self,x):
        self.next = None
        self.val = x
        self.min = x
        
class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m = max
        self.head = None
        
    def push(self, x):

        new = ListNode(x)
        new.next = self.head
        self.head = new
        if x < self.m:
            self.m = x
        new.min = self.m
        

    def pop(self):
        p = -1
        if self.head != None:
            p = self.head.val
            self.head = self.head.next
        if self.head != None:
            self.m = self.head.min
        else : 
            self.m = max
        return p

    def top(self):
        return self.head.val

    def getMin(self):
        return self.m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Python3 双栈法
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        lastMin = self.min[-1] if self.min else float("inf")
        sef.min.append(min(lastMin, x))

    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]