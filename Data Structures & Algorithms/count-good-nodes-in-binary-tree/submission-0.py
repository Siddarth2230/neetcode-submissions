# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, maxNode, res):
        if not root:
            return
        
        if root.val >= maxNode:
            res.append(root.val)
            maxNode = root.val
        
        self.dfs(root.right, maxNode, res)
        self.dfs(root.left, maxNode, res)

    def goodNodes(self, root: TreeNode) -> int:
        maxNode = root.val
        res = []
        self.dfs(root, maxNode, res)

        return len(res)
        