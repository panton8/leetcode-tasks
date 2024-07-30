from collections import Counter
from typing import List


class Solution:
    # M(n)
    def singleNumber1(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)

        for key in nums_counter:
            if nums_counter[key] == 1:
                return key

    # M(1)
    def singleNumber2(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res


def main():
    sol = Solution()
    nums1 = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    nums3 = [1]

    assert sol.singleNumber1(nums1) == 1
    assert sol.singleNumber1(nums2) == 4
    assert sol.singleNumber1(nums3) == 1

    assert sol.singleNumber2(nums1) == 1
    assert sol.singleNumber2(nums2) == 4
    assert sol.singleNumber2(nums3) == 1


if __name__ == '__main__':
    main()
