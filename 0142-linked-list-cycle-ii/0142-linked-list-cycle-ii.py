# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def findLength(slow_p):
            stationary = slow_p
            pointer = slow_p.next
            length = 1
            while pointer != stationary:
                pointer = pointer.next
                length += 1
            return length
        
        def findHead (head, slow_p):
            length = findLength(slow_p)
            ahead = head
            behind = head
            for i in range(length):
                ahead = ahead.next
            while True:
                if ahead == behind:
                    return behind
                ahead = ahead.next
                behind = behind.next

                
        fast_p = head
        slow_p = head
        while fast_p and fast_p.next and fast_p.next.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if fast_p == slow_p:
                return findHead(head, slow_p)
        return None
        
        