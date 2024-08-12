from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_counter = {}

        for num in nums:
            nums_counter[num] = nums_counter.get(num, 0) + 1

        pairs = 0

        for key in nums_counter:
            pairs += self.count_pairs(nums_counter[key])

        return pairs

    def count_pairs(self, num: int):
        return (num * (num - 1)) // 2


def main():
    sol = Solution()

    assert sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert sol.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert sol.numIdenticalPairs([1, 2, 3]) == 0


if __name__ == '__main__':
    main()
