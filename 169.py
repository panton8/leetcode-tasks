import math
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        min_majority_len = math.ceil(len(nums) / 2)
        print(min_majority_len)

        for num in nums_counter:
            if nums_counter[num] >= min_majority_len:
                return num


def main():
    sol = Solution()
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    nums3 = [8, 8, 7, 7, 7]

    assert sol.majorityElement(nums1) == 3
    assert sol.majorityElement(nums2) == 2
    assert sol.majorityElement(nums3) == 7


if __name__ == '__main__':
    main()