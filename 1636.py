class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        reps = {}

        for num in nums:
            reps[num] = reps.get(num, 0) + 1

        seq = sorted(reps, key=lambda item: (reps[item], -item))
        new_nums = []

        for num in seq:
            new_nums.extend([num] * reps[num])

        return new_nums

    def frequencySort_2(self, nums: list[int]) -> list[int]:
        reps = {}

        for num in nums:
            reps[num] = reps.get(num, 0) + 1

        seq = sorted(nums, key=lambda x: (reps[x], -x))

        return seq


def main():
    sol = Solution()
    nums_1 = [1, 1, 2, 2, 2, 3]
    nums_2 = [2, 3, 1, 3, 2]
    assert sol.frequencySort(nums_1) == [3, 1, 1, 2, 2, 2]
    assert sol.frequencySort(nums_2) == [1, 3, 3, 2, 2]
    assert sol.frequencySort_2(nums_1) == [3, 1, 1, 2, 2, 2]
    assert sol.frequencySort_2(nums_2) == [1, 3, 3, 2, 2]


if __name__ == '__main__':
    main()
