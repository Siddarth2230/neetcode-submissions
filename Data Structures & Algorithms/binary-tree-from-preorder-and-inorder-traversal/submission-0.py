# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Tree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, mp):
        if preStart > preEnd or inStart > inEnd:
            return None
        
        root = TreeNode(preorder[preStart])
        inRoot = mp[root.val]
        numsLeft = inRoot - inStart

        root.left = self.Tree(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1, mp)
        root.right = self.Tree(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, mp)

        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = defaultdict()
        n = len(inorder)
        
        for i in range(n):
            mp[inorder[i]] = i
        
        root = self.Tree(preorder, 0, n-1, inorder, 0, n-1, mp)

        return root
