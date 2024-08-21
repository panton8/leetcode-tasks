from typing import List


class Solution:
    # O(nlogn)
    def longestConsecutive1(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        curr = nums[0]
        max_long = 0
        curr_long = 0

        for num in nums[1:]:
            if curr == num - 1:
                curr_long += 1
            else:
                max_long = max(max_long, curr_long)
            curr = num

        max_long = max(max_long, curr_long)

        return max_long+1

    # O(n)
    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)
        max_long = 0

        for num in nums:
            if num - 1 not in nums:
                curr_seq_len = 1
                while num + 1 in nums:
                    curr_seq_len += 1
                    num += 1
                max_long = max(max_long, curr_seq_len)

        return max_long


def main():
    sol = Solution()
    nums1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums2 = [1, 0, 1, 2]

    assert sol.longestConsecutive1(nums1) == 9
    assert sol.longestConsecutive1(nums2) == 3

    assert sol.longestConsecutive2(nums1) == 9
    assert sol.longestConsecutive2(nums2) == 3


if __name__ == '__main__':
    main()
    