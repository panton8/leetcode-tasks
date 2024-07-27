class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg_value = float('-inf')
        curr_sum = 0
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_avg_value = max(curr_sum / k, max_avg_value)
                curr_sum -= nums[left]
                left += 1

        return max_avg_value


def main():
    nums_1 = [1, 12, -5, -6, 50, 3]
    k_1 = 4
    nums_2 = [5]
    k_2 = 1

    sol = Solution()
    assert sol.findMaxAverage(nums_1, k_1) == 12.75
    assert sol.findMaxAverage(nums_2, k_2) == 5.0


if __name__ == '__main__':
    main()
