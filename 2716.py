class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


def main():
    sol = Solution()

    assert sol.minimizedStringLength('aabbbb') == 2
    assert sol.minimizedStringLength('abab') == 2
    assert sol.minimizedStringLength('cbdba') == 4


if __name__ == '__main__':
    main()
