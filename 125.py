class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = ''

        for c in s:
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                only_letters = only_letters + c.lower()

        return only_letters == only_letters[::-1]


def main():
    s1 = 'A man, a plan, a canal: Panama'
    s2 = 'race a car'
    s3 = ''
    s4 = '0P'
    s5 = '121'

    solution = Solution()

    assert solution.isPalindrome(s1) is True
    assert solution.isPalindrome(s2) is False
    assert solution.isPalindrome(s3) is True
    assert solution.isPalindrome(s4) is False
    assert solution.isPalindrome(s5) is True


if __name__ == '__main__':
    main()
