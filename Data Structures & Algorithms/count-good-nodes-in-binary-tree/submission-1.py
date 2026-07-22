# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxVal):
            if not root:
                return 0
            
            count = 0
            if root.val >= maxVal:
                count = 1
                maxVal = root.val
            
            count += dfs(root.left, maxVal)
            count += dfs(root.right, maxVal)

            return count
        
        return dfs(root, root.val)
    
    # TC - O(N) - we traverse each node
    # SC - O(H) - Recursion stack space (recursion calls), O(N) for skewed tree and O(log(n)) for balanced binary tree
        