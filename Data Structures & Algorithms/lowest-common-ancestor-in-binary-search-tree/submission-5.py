# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p
        self.q = q
        self.result = -1

        self.containsAncestors(root)
        return self.result

    def containsAncestors(self, root):
        if root == None:
            return (False, False)
        
        if self.result != -1:
            return (True, True)
        
        pf = False
        qf = False
        
        if self.p.val == root.val:
            pf = True
        elif self.q.val == root.val:
            qf = True
        
        left_result = self.containsAncestors(root.left)
        if left_result == (True, True):
            return left_result

        right_result = self.containsAncestors(root.right)
        if right_result == (True, True):
            return right_result

        if left_result[0] != right_result[0] and left_result[1] != right_result[1]:
            self.result = root
        
        qf = qf or left_result[1] or right_result[1]
        pf = pf or left_result[0] or right_result[0]

        if pf == True and qf == True:
            self.result = root
        
        return (pf, qf)