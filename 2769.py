class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t


def main():
    sol = Solution()

    assert sol.theMaximumAchievableX(4, 1) == 6
    assert sol.theMaximumAchievableX(3, 2) == 7
    assert sol.theMaximumAchievableX(5, 6) == 17


if __name__ == '__main__':
    main()

