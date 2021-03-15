class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ids = {}

        def union(edge1, edge2):
            parent1 = find(edge1)
            parent2 = find(edge2)
            ids[parent1] = parent2

        def find(edge):
            if edge != ids[edge]:
                ids[edge] = find(ids[edge])
            return ids[edge]

        for edge in edges:
            if edge[0] not in ids:
                ids[edge[0]] = edge[0]

            if edge[1] not in ids:
                ids[edge[1]] = edge[1]

            if find(edge[1]) == find(edge[0]):
                return edge

            # join two eges
            union(edge[1], edge[0])

        return [0, 0]
