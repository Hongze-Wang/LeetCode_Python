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
        
        pre, cur = None, head
        
        while m > 1:         # 移动到逆置起始结点
            pre = cur
            cur = cur.next;
            m, n = m-1, n-1
            
        con, tail = pre, cur # pre指向左边未逆置部分 cur指向第一个逆置结点 con, tail保存这两个指针
        
        while n:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            n -= 1           # 利用pre, cur逆置 标准逆置代码
            
        if con:              # 边界判断 不是从头结点就开始逆置的
            con.next = pre   # 连接左边未逆置部分
        else:
            head = pre       # 从头结点开始逆置 则重置投结点为pre
        
        tail.next = cur      # 连接右边未逆置部分
        
        return head
