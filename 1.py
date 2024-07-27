class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        target_indexes = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in target_indexes:
                return [target_indexes[diff], i]
            target_indexes[nums[i]] = i


def main():
    nums_1 = [2, 7, 11, 15]
    target_1 = 9
    nums_2 = [3, 2, 4]
    target_2 = 6
    nums_3 = [3, 3]
    target_3 = 6

    assert Solution().twoSum(nums_1, target_1) == [0, 1]
    assert Solution().twoSum(nums_2, target_2) == [1, 2]
    assert Solution().twoSum(nums_3, target_3) == [0, 1]


if __name__ == '__main__':
    main()
