# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return None
        rear = head
        
        while rear.next != None:
            if rear.val == rear.next.val:
                rear.next = rear.next.next
            else:
                rear = rear.next
                
        return head
        