# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare(p,q):
            if q == None and p == None:
                return True
            if (p and q == None) or (q and p == None) or (q.val != p.val):
                return False
            
            left = compare(p.left, q.left)
            if not left:
                return False
            
            right = compare(p.right, q.right)
            if not right:
                return False
            
            return True
        
        return compare(p,q)
            

        