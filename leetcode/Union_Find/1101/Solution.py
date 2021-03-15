class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort()
        ids = [i for i in range(N)]
        groups = N

        def union(edge1, edge2) -> None:
            parent1 = find(edge1)
            parent2 = find(edge2)
            ids[parent1] = parent2

        def find(edge) -> int:
            if edge != ids[edge]:
                ids[edge] = find(ids[edge])
            return ids[edge]

        for entry in logs:

            time_stamp = entry[0]

            A = entry[1]
            B = entry[2]

            if find(A) != find(B):
                union(A, B)
                groups -= 1

            if groups == 1:
                return time_stamp

        return -1
