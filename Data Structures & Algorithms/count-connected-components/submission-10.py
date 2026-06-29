class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [i for i in range(n)]


        def find(n1):
            res = n1

            while res != nodes[res]:
                res = nodes[res]
            
            return res

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return 0
            else:
                nodes[r2] = r1
                return 1

        res = 0

        for edge in edges:
            res += union(edge[0], edge[1])

        return n - res