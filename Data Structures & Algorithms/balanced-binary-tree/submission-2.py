# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def calculateHeight(node, height):
            if node == None:
                return height
            if self.valid == False:
                return height

            height += 1

            lh = calculateHeight(node.left, height)
            rh = calculateHeight(node.right, height)

            if abs(lh - rh) > 1:
                self.valid = False
                return height
            
            return max(lh, rh)

        calculateHeight(root, 0)

        return self.valid