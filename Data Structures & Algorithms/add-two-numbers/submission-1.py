# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dNode = ListNode(-1)
        res = dNode
        t1, t2 = l1, l2
        carry = 0

        while t1 and t2:
            curr_sum = t1.val + t2.val + carry

            value = curr_sum % 10
            carry = curr_sum // 10

            newNode = ListNode(value)
            res.next = newNode

            t1, t2, res = t1.next, t2.next, res.next
        
        while t1:
            curr_sum = t1.val + carry

            value = curr_sum % 10
            carry = curr_sum // 10

            newNode = ListNode(value)
            res.next = newNode

            t1, res = t1.next, res.next
        
        while t2:
            curr_sum = t2.val + carry

            value = curr_sum % 10
            carry = curr_sum // 10

            newNode = ListNode(value)
            res.next = newNode

            t2, res = t2.next, res.next

        if carry != 0:
            newNode = ListNode(carry)
            res.next = newNode
        
        return dNode.next

        