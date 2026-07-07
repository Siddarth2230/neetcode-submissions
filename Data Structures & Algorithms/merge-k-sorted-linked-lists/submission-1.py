# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        t1, t2 = list1, list2
        dNode = ListNode(-1)
        temp = dNode

        while t1 and t2: 
            if t1.val < t2.val:
                temp.next = t1
                t1 = t1.next
                temp = temp.next
            else:
                temp.next = t2
                t2 = t2.next
                temp = temp.next

        if t1:
            temp.next = t1
        else:
            temp.next = t2
        
        return dNode.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None

        for lst in lists:
            merged = self.mergeTwoLists(merged, lst)

        return merged
                    

                     
                

                    








        
        
        