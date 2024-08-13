from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_counter = {}

        for num in arr:
            num_counter[num] = num_counter.get(num, 0) + 1

        lucky_num = -1

        for key in num_counter:
            if num_counter[key] == key:
                lucky_num = max(key, lucky_num)

        return lucky_num


def main():
    sol = Solution()

    assert sol.findLucky([2, 2, 3, 4]) == 2
    assert sol.findLucky([1, 2, 2, 3, 3, 3]) == 3
    assert sol.findLucky([3, 4, 4, 1, 1, 1, 1, 7, 7]) == -1
    print(chr(ord('a')+1))


if __name__ == '__main__':
    main()
