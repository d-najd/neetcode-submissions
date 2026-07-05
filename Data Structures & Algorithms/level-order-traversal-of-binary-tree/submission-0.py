# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque()
        result = []
        
        queue.append(root)
      #  level = 0
        while len(queue) != 0:
            queue_size = len(queue)

            cur_level_list = []

            for i in range(queue_size):
                cur = queue.popleft()
                
                if cur.left != None:
                    queue.append(cur.left)

                if cur.right != None:
                    queue.append(cur.right)

                cur_level_list.append(cur.val)

            result.append(cur_level_list)      

           # level += 1
        return result 
