class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ids = {}

        def union(edge1, edge2) -> None:
            parent1 = find(edge1)
            parent2 = find(edge2)
            ids[parent1] = parent2

        def find(edge) -> str:
            if edge != ids[edge]:
                ids[edge] = find(ids[edge])
            return ids[edge]

        not_equal = []
        for eq in equations:
            lhs = eq[0]
            rhs = eq[3]
            sign = eq[1:3]

            if lhs not in ids:
                ids[lhs] = lhs

            if rhs not in ids:
                ids[rhs] = rhs

            if sign == '==':
                union(lhs, rhs)

            if sign == '!=':
                not_equal.append(eq)

        for eq in not_equal:
            if find(eq[0]) == find(eq[-1]):
                return False

        return True
