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
        
        print(f"TESTING {root.val}")
        if self.result != -1:
            return (False, False)
        
        pf = False
        qf = False
        
        if self.p.val == root.val:
            pf = True
        elif self.q.val == root.val:
            qf = True
        
        left_result = self.containsAncestors(root.left)
        right_result = self.containsAncestors(root.right)
        
        print(f"tw {root.val} {left_result} {right_result} {pf} {qf}")

        if left_result == (True, True):
            return left_result
        elif right_result == (True, True):
            return right_result

        if left_result[0] != right_result[0] and left_result[1] != right_result[1]:
            self.result = root
            print("SET 1")
        elif left_result[0] == True and qf == True or left_result[1] == True and pf == True:
            self.result = root
            print("SET 2")
        elif right_result[0] == True and qf == True or right_result[1] == True and pf == True:
            self.result = root
            print("SET 3")

        print("END")
        return (pf or left_result[0] or right_result[0], qf or left_result[1] or right_result[1])
