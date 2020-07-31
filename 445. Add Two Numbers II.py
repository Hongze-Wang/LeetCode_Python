# 445. Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNumber(self, root):
        num = 0
        while root:
            num = num*10 + root.val
            root = root.next
        return num
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = str(self.getNumber(l1) + self.getNumber(l2))
        head = ListNode(0)
        cur = head
        for char in res:
            cur.next = ListNode(int(char))
            cur = cur.next
        return head.next
