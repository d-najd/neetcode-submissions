class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [i for i in range(n)]

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
            
            print(f"n1 {n1} {n1p} n2 {n2} {n2p}")
            nodes[n2p] = n1p
            print(nodes)

        for n1, n2 in edges:
            if (union(n1, n2) == False):
                return False

        for i in range(1, len(nodes)):
            if find(nodes[i]) != find(nodes[0]):
                return False
            
        return True