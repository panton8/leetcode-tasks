from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total_sum = 0
        min_len = len(nums) + 1

        for r in range(len(nums)):
            total_sum += nums[r]
            while total_sum >= target:
                min_len = min(min_len, r - l + 1)
                total_sum -= nums[l]
                l += 1

        if min_len > len(nums):
            return 0
        return min_len


def main():
    sol = Solution()
    arr1 = [2, 3, 1, 2, 4, 3]
    arr2 = [1, 4, 4]
    arr3 = [1, 1, 1, 1, 1, 1, 1, 1]
    arr4 = [1, 2, 3, 4, 5]

    assert sol.minSubArrayLen(7, arr1) == 2
    assert sol.minSubArrayLen(4, arr2) == 1
    assert sol.minSubArrayLen(11, arr3) == 0
    assert  sol.minSubArrayLen(11, arr4) == 3


if __name__ == '__main__':
    main()