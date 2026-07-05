# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.calDepth(root, 0)
        return self.depth

    def calDepth(self, root, curDepth):
        if root == None:
            return

        curDepth += 1
        if curDepth > self.depth:
            self.depth = curDepth
        
        self.calDepth(root.left, curDepth)
        self.calDepth(root.right, curDepth)
        
