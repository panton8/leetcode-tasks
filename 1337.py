from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indexed_mat = [(row, idx) for idx, row in enumerate(mat)]

        indexed_mat.sort()

        return [mat[1] for mat in indexed_mat[:k]]


def main():
    sol = Solution()

    mat1 = [[1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1]]
    k1 = 3

    mat2 = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0]]
    k2 = 2

    assert sol.kWeakestRows(mat1, k1) == [2, 0, 3]
    assert sol.kWeakestRows(mat2, k2) == [0, 2]


if __name__ == "__main__":
    main()
