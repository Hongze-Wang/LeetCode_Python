# 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(left, right): # merge two sorted list
            dummy = cur = ListNode(0)
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            if left:
                cur.next = left
            if right:
                cur.next = right
            return dummy.next

        def mergeSort(head):
            if not head or not head.next:
                return head
            
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            new_head = slow.next
            slow.next = None
            
            left = mergeSort(head)      # keep split half
            right = mergeSort(new_head) # keep split half
            return merge(left, right)

        return mergeSort(head)
