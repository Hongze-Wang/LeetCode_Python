# 23. Merge k Sorted Lists

# Using Merge Two List and Divide And Conquer

'''
0 1
2 3
4 5
6 7
8 9
0 2
4 6
8 10
0 4
8 12
0 8
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, l1, l2):
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
            
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if k > 0 else lists
        
    
