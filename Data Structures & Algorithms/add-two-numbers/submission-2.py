# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dNode = ListNode(-1)
        t1, t2, res = l1, l2, dNode
        carry = 0

        while t1 or t2 or carry:
            v1 = t1.val if t1 else 0
            v2 = t2.val if t2 else 0

            curr_sum = v1 + v2 + carry

            carry = curr_sum // 10
            digit = curr_sum % 10

            res.next = ListNode(digit)
            res = res.next

            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
        
        return dNode.next

        
        