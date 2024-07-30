from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        nums_squares = [0] * len(nums)
        index = len(nums) - 1

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                nums_squares[index] = nums[r] ** 2
                r -= 1
            else:
                nums_squares[index] = nums[l] ** 2
                l += 1
            index -= 1

        return nums_squares


def main():
    sol = Solution()

    nums1 = [-4, -1, 0, 3, 10]
    nums2 = [-7, -3, 2, 3, 11]

    assert sol.sortedSquares(nums1) == [0, 1, 9, 16, 100]
    assert sol.sortedSquares(nums2) == [4, 9, 9, 49, 121]


if __name__ == '__main__':
    main()
