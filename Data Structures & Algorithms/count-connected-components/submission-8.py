class Node:
    root: None

    def __init__(self):
        self.root = None

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [i for i in range(n)]

        def find(n1):
            res = n1

            while res != nodes[res]:
                res = nodes[res]

            return res

        def merge(n1, n2):
            r1 = find(n1)
            r2 = find(n2)

            #print(f"test {r1} {r2} for {n1} {n2}")
            #print(nodes)

            if r1 == r2:
                return 0
            else:
                nodes[r2] = r1
                return 1

        res = n
        for n1, n2 in edges:
            res -= merge(n1, n2)
        
        return res