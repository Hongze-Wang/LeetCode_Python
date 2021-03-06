# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        rear = head
        while l1 and l2:
            if l1.val < l2.val:
                rear.next = l1
                l1 = l1.next
                rear = rear.next
            else:
                rear.next = l2
                l2 = l2.next
                rear = rear.next
    
        if l1 is None:
            rear.next = l2
        else:
            rear.next = l1

        return head.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = head = ListNode(-1);
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head.next
