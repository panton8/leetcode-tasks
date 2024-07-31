from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)

        if nums_len < 2:
            return
        l, r = 0, 1

        while r != nums_len:
            if nums[l] == 0 and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r += 1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            else:
                l += 1
                r += 1


def main():
    sol = Solution()

    nums1 = [0, 1, 0, 3, 12]
    nums2 = [0]
    nums3 = [1, 2, 0, 0, 3]

    sol.moveZeroes(nums1)
    sol.moveZeroes(nums2)
    sol.moveZeroes(nums3)

    assert nums1 == [1, 3, 12, 0, 0]
    assert nums2 == [0]
    assert nums3 == [1, 2, 3, 0, 0]


if __name__ == '__main__':
    main()
