from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        is_odd = False
        symbol_counter = Counter(s)
        res = 0

        for key in symbol_counter:
            if symbol_counter[key] % 2 == 0:
                res += symbol_counter[key]
            else:
                res += symbol_counter[key] - 1
                is_odd = True

        if is_odd:
            res += 1

        return res


def main():
    sol = Solution()
    s1 = 'abccccdd'
    s2 = 'a'
    s3 = 'qqwwwddddddd'

    assert sol.longestPalindrome(s1) == 7
    assert sol.longestPalindrome(s2) == 1
    assert sol.longestPalindrome(s3) == 11


if __name__ == '__main__':
    main()
