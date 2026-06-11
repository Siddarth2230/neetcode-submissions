# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
    
        length = 0
        # find length of linked list
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # position from start (1 based indexing)
        pos = length - n + 1

        if pos == 1:
            temp = head.next
            head.next = None
            head = temp
        elif pos == length:
            temp = head
            prev = None

            while temp.next:
                prev = temp
                temp = temp.next
            
            prev.next = None
        else:
            temp = head
            prev = None
            i = 1
            while i != pos:
                prev = temp
                temp = temp.next
                i += 1
            
            prev.next = temp.next
            temp.next = None
        
        return head
            


        