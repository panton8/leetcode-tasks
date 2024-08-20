from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l, r = 0, 0
        nums_len = len(nums)
        res = 0

        while r < nums_len:
            if not self.valid_conditions(l, r, nums_len, nums, threshold, res):
                if l == r:
                    r += 1
                l = r
                continue
            res = max(res, r - l + 1)
            r += 1

        return res

    def valid_conditions(self, l, r, nums_len, nums, threshold, res):
        if nums[l] % 2 != 0:
            return False

        if r - l + 1 > 1 and nums[r-1] % 2 == nums[r] % 2:
            return False

        if nums[r] > threshold:
            return False

        return True


def main():
    sol = Solution()
    nums1 = [3, 2, 5, 4]
    nums2 = [1, 2]
    nums3 = [2, 3, 4, 5]
    nums4 = [2, 8]
    nums5 = [2, 2]
    nums6 = [4, 10, 3]

    assert sol.longestAlternatingSubarray(nums1, 5) == 3
    assert sol.longestAlternatingSubarray(nums2, 2) == 1
    assert sol.longestAlternatingSubarray(nums3, 4) == 3
    assert sol.longestAlternatingSubarray(nums4, 4) == 1
    assert sol.longestAlternatingSubarray(nums5, 18) == 1
    assert sol.longestAlternatingSubarray(nums6, 10) == 2


if __name__ == '__main__':
    main()
