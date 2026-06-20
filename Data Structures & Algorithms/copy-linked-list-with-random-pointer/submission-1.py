"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head

        while temp:
            copy = Node(temp.val)
            copy.next = temp.next
            temp.next = copy
            
            temp = temp.next.next
        
        # connect random
        temp = head

        while temp:
            copy = temp.next

            if not temp.random:
                copy.random = temp.random
            else:
                copy.random = temp.random.next
            
            temp = temp.next.next
        
        # connect next
        temp = head
        dummyNode = Node(-1)
        res = dummyNode

        while temp:
            res.next = temp.next
            temp.next = temp.next.next

            temp, res = temp.next, res.next
    
        return dummyNode.next

        
        
