from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def main():
    sol = Solution()
    arr_1 = [1, 2, 3, 1]
    arr_2 = [1, 2, 3, 4]
    arr_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    assert sol.containsDuplicate(arr_1) is True
    assert sol.containsDuplicate(arr_2) is False
    assert sol.containsDuplicate(arr_3) is True


if __name__ == '__main__':
    main()
