from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1

        return -1


def main():
    nums_1 = [-1, 0, 3, 5, 9, 12]
    target_1 = 9
    nums_2 = [-1, 0, 3, 5, 9, 12]
    target_2 = 2

    assert Solution().search(nums_1, target_1) == 4
    assert Solution().search(nums_2, target_2) == -1


if __name__ == '__main__':
    main()

