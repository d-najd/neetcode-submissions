# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        
        result = []
        result.append(root.val)
        self.serializeRecurse(root, result)

        parsed = ""
        for cur in result:
            
            if cur == None:
                parsed += ":"
                continue
            parsed += f"{cur}:"
        return parsed

    def serializeRecurse(self, cur: Optional[TreeNode], result):
        if cur != None:
            if cur.left != None:
                result.append(cur.left.val)
            else:
                result.append(None)
            if cur.right != None:
                result.append(cur.right.val)
            else:
                result.append(None)
            self.serializeRecurse(cur.left, result)
            self.serializeRecurse(cur.right, result)
    
    counter = 1
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if "":
            return None
        
        test = data.split(":")
        result = TreeNode(test[0])
        self.deserializeBuilder(result, test)

        return result
    
    def deserializeBuilder(self, cur, test):
        if self.counter + 1 >= len(test):
            return 

        if cur != None:
            lv = None
            rv = None
            if test[self.counter] != '':
                lv = TreeNode(int(test[self.counter]))
            if test[self.counter+1] != '':
                rv = TreeNode(int(test[self.counter+1]))

            cur.left = lv
            cur.right = rv
            self.counter += 2
            self.deserializeBuilder(cur.left, test)
            self.deserializeBuilder(cur.right, test)
