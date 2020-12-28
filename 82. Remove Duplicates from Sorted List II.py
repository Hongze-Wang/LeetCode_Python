# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        dummyHead = ListNode(-1)
        dummyHead.next = head
        pre, cur, nex = dummyHead, head, head.next
        
        while cur and nex:                    # 使用链表节点的数据域 都应当先判断节点是否为空
            val = cur.val
            if cur.val == nex.val:
                while nex and nex.val == val: # 使用链表节点的数据域 都应当先判断当前节点是否为空 每一次移动节点之后都应当再次判断
                    nex = nex.next
                cur = nex
                if nex:                       # 使用链表节点的数据域 都应当先判断当前节点是否为空 每一次移动节点之后都应当再次判断
                    nex = nex.next
                pre.next = cur
            else:
                pre = cur
                cur = nex
                nex = nex.next
        
        return dummyHead.next