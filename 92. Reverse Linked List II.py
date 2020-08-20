# 92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 72% faster
# Recusion
# class Solution:
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if not head:
#             return None
#         left, right = head, head
#         stop = False
#         def recurseAndReverse(right, m, n):
#             nonlocal left, stop
            
#             if n == 1:
#                 return
#             right = right.next
            
#             if m > 1:
#                 left = left.next # reach m node need m-1 moves
#             recurseAndReverse(right, m-1, n-1)
            
#             if left == right or right.next == left: # right.next == left 防止重复交换
#                 stop = True
#             if not stop:
#                 left.val, right.val = right.val, left.val
#                 left = left.next
        
#         recurseAndReverse(right, m, n)
#         return head

# Iteration
class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
            return None
        
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m-1, n-1
            
        tail, con = cur, prev
        
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
            
        if con:              # if more than one node
            con.next = prev  # connext the reversed part with unreversed part
        else:
            head = prev
        tail.next = cur # connect remain part
            
        return head
