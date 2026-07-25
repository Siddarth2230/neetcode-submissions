# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        def maxPath(root):
            if not root:
                return 0
            
            leftSum = maxPath(root.left)
            rightSum = maxPath(root.right)
            self.maxi = max(self.maxi, leftSum + rightSum + root.val)

            return max(0, root.val + max(leftSum, rightSum))
        
        maxPath(root)
        return self.maxi
