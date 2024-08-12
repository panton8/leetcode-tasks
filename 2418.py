from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_by_name = {}

        for name, height in zip(names, heights):
            height_by_name[height] = name

        res = []

        heights.sort(key=lambda x: -x)
        for h in heights:
            res.append(height_by_name[h])

        return res


def main():
    sol = Solution()

    assert sol.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]) == ['Mary', 'Emma', 'John']


if __name__ == '__main__':
    main()
