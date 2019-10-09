# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        
        if not head:
            return None

        cur = head
        while(cur.next):
            if cur.next.val == val:
                cur.next = cur.next.next;
            else:
                cur = cur.next
        return head