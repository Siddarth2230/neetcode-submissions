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
        mp = {}
        
        # Store { original : copy }
        temp = head
        while temp:
            copyNode = Node(temp.val)
            mp[temp] = copyNode
            temp = temp.next

        temp = head
        while temp:
            copy = mp[temp]
            copy.next = mp.get(temp.next)
            copy.random = mp.get(temp.random)
            temp = temp.next
        
        return mp.get(head)

        
        
