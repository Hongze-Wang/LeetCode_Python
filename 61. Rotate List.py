# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# k rotations equivlent to k % len

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head

        count = head
        length = 0
        
        while count is not None:
            count = count.next
            length += 1
        
        num = k % length
        for _ in range(num):
            curr = head
            while curr.next.next is not None:
                curr = curr.next
            temp = curr.next
            curr.next = None
            temp.next = head
            head = temp
        return head
