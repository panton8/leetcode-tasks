from typing import List
from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(set(nums))

        nums_counter = Counter(nums)

        smaller_than = {}
        small_count = 0

        for num in sort_nums:
            smaller_than[num] = small_count
            small_count += nums_counter[num]


        res = []
        for num in nums:
            res.append(smaller_than[num])

        return res


def main():
    sol = Solution()

    assert sol.smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]


if __name__ == '__main__':
    main()