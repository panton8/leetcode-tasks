from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_nullable = [False] * len(matrix)
        col_nullable = [False] * len(matrix[0])
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    row_nullable[i] = True
                    col_nullable[j] = True

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if row_nullable[i]:
                    matrix[i][j] = 0
                if col_nullable[j]:
                    matrix[i][j] = 0


def main():
    sol = Solution()
    matrix_a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix_b = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

    sol.setZeroes(matrix_a)
    sol.setZeroes(matrix_b)



if __name__ == "__main__":
    main()
