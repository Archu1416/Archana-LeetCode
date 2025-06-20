class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        r = [1] * rows
        c = [1] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r[i] = 0
                    c[j] = 0

        for i in range(rows):
            for j in range(cols):
                if r[i] == 0 or c[j] == 0:
                    matrix[i][j] = 0