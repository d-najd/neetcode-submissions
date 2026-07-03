class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [i for i in range(n)]
        children = [1 for i in range(n)]

        def find(n1):
            cur = n1

            while nodes[cur] != cur:
                cur = find(nodes[cur])

            return cur
        def union(n1, n2):
            n1p = find(n1)
            n2p = find(n2)

            if n1p == n2p:
                return False
            
            if (children[n2p] > children[n1p]):
                nodes[n2p] = n1p
                children[n2p] += 1
            else:
                nodes[n1p] = n2p
                children[n1p] += 1

        for n1, n2 in edges:
            if (union(n1, n2) == False):
                return False
        
        firstNodeRoot = find(nodes[0])

        for i in range(1, len(nodes)):
            if find(nodes[i]) != firstNodeRoot:
                return False
            
        return True