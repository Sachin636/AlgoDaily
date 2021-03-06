class Solution:
    def bubble_sort(self, indices: List[int]) -> None:
        for i in range(len(indices)):
            for j in range(i+1, len(indices)):
                x = indices[i]
                y = indices[j]
                if self.mat[x[0]][x[1]] > self.mat[y[0]][y[1]]:
                    self.mat[x[0]][x[1]], self.mat[y[0]][y[1]
                                                         ] = self.mat[y[0]][y[1]], self.mat[x[0]][x[1]]

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        self.mat = mat
        diag = {i-j: [] for i in range(m) for j in range(n)}
        for i in range(m):
            for j in range(n):
                diag[i - j].append((i, j))

        for k in diag.keys():
            self.sort(diag[k])

        return self.mat
