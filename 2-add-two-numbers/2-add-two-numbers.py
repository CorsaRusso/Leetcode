# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        retval = ListNode()
        pointer = retval
        while(l1 != None or l2 != None):
            pointer.next = ListNode()
            pointer = pointer.next
            if(l1 == None):
                temp = l2.val + carry
                carry = temp // 10
                pointer.val = temp % 10
                l2 = l2.next
            elif(l2 == None):
                temp = l1.val + carry
                carry = temp // 10
                pointer.val = temp % 10
                l1 = l1.next
            else:
                temp = l1.val + l2.val + carry
                carry = temp // 10
                pointer.val = temp % 10
                l1 = l1.next
                l2 = l2.next
            # print(l1)
            # print(l2)
            # print(retval)
            # print("---")
        if(carry != 0):
            pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = carry
        return retval.next