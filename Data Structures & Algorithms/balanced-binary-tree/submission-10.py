# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def calculateHeight(node):
            if self.valid == False:
                return -1
            if node == None:
                return 0

            lh = calculateHeight(node.left)
            rh = calculateHeight(node.right)

            if abs(lh - rh) > 1:
                self.valid = False
                return -1
            
            return max(lh, rh) + 1

        calculateHeight(root)

        return self.valid