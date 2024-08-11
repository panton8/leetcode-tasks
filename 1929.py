from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)

        return ans


def main():
    sol = Solution()

    assert sol.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert sol.getConcatenation([1, 2, 3]) == [1, 2, 3, 1, 2, 3]


if __name__ == '__main__':
    main()
