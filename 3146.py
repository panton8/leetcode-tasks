class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = i

        diff = 0

        for i in range(len(t)):
            diff += abs(s_dict[t[i]] - i)

        return diff


def main():
    sol = Solution()

    assert sol.findPermutationDifference('abc', 'bac') == 2
    assert sol.findPermutationDifference('abcde', 'edbac') == 12


if __name__ == '__main__':
    main()
