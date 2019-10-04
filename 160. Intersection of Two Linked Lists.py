# 160. Intersection of Two Linked Lists

# Python 2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1 = headA
        node2 = headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1

# Using set, similarly you cas use hashset in Java
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        cache = set()
        while headA:
            cache.add(headA)
            headA = headA.next
        while headB:
            if headB in cache:
                return headB
            headB = headB.next
        return None