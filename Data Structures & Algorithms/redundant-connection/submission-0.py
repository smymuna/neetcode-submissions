class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False
            
            if size[root1] < size[root2]:
                parent[root1] = root2
                size[root2] += size[root1]

            else:
                parent[root2] = root1
                size[root1] += size[root2]

            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]