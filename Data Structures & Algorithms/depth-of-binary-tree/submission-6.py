# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calDepth(root, 0)

    def calDepth(self, root, curDepth):
        if root == None:
            return curDepth

        curDepth += 1
        
        return max(self.calDepth(root.left, curDepth), self.calDepth(root.right, curDepth))        
