# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        self.helper(root)
        return self.diameter

    def helper(self, root):
        ld = 0
        rd = 0

        if root.left != None:
            ld = self.helper(root.left) + 1
        if root.right != None:
            rd = self.helper(root.right) + 1

        maxV = ld + rd
        if maxV > self.diameter:
            self.diameter = maxV
        
        return max(ld, rd)
