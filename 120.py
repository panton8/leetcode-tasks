from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_tree = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for index, num in enumerate(row):
                min_tree[index] = num + min(min_tree[index], min_tree[index + 1])

        return min_tree[0]


def main():
    sol = Solution()
    triangle_a = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle_b = [[-10]]
    triangle_c = [[-1], [2, 3], [1, -1, -3]]

    assert sol.minimumTotal(triangle_a) == 11
    assert sol.minimumTotal(triangle_b) == -10
    assert sol.minimumTotal(triangle_c) == -1


if __name__ == '__main__':
    main()
