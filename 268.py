from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        needed_sum = sum(range(len(nums)+1))

        return needed_sum - nums_sum


def main():
    sol = Solution()
    nums1 = [3, 0, 1]
    nums2 = [0, 1]
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    nums4 = [0]

    assert sol.missingNumber(nums1) == 2
    assert sol.missingNumber(nums2) == 2
    assert sol.missingNumber(nums3) == 8
    assert sol.missingNumber(nums4) == 1


if __name__ == '__main__':
    main()
