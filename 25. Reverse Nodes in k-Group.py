# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLen(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k <= 0:
            return None
        pre, cur, nex = None, None, head
        count = 0
        while nex and count < k:
            pre = cur
            cur = nex
            nex = nex.next
            cur.next = pre
            count += 1
        
        if nex:
            length = self.getLen(nex)
            if k > length:
                head.next = nex
            else:
                head.next = self.reverseKGroup(nex, k)

# optimized
class Solution:
    def getLength(self, head):
        length = 0
        
        while head:
            length += 1
            head = head.next
            
        return length
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k < 0:
            return
        
        pre, cur, nex = None, None, head
        count = 0
        while nex and count < k:
            pre = cur
            cur = nex
            nex = cur.next
            cur.next = pre
            count += 1
    
        if k > self.getLength(nex):
            head.next = nex
        else:
            head.next = self.reverseKGroup(nex, k)
            
        return cur
        return cur
