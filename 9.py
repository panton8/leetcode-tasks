class Solution:
    # M: O(n) T: O(n)
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False

        copy_x = x
        digits = []

        while copy_x > 0:
            digits.append(copy_x % 10)
            copy_x = copy_x // 10

        max_pow = 10 ** (len(digits) - 1)

        reverse_x = 0

        for digit in digits:
            reverse_x += digit * max_pow
            max_pow /= 10

        return x == reverse_x

    # M: O(1) T: O(n)
    def isPalindrome2(self, x: int) -> bool:

        if x < 0:
            return False

        copy_x = x
        x_len = -1

        while copy_x > 0:
            copy_x = copy_x // 10
            x_len += 1

        copy_x = x
        reverse_x = 0
        digit_pow = 1

        while copy_x > 0:
            reverse_x += (copy_x // 10**x_len) * digit_pow
            copy_x = copy_x % 10**x_len
            x_len -= 1
            digit_pow *= 10

        return x == reverse_x


def main():
    sol = Solution()

    x1 = 121
    x2 = -121
    x3 = 1
    x4 = 145

    assert sol.isPalindrome1(x1) is True
    assert sol.isPalindrome1(x2) is False
    assert sol.isPalindrome1(x3) is True
    assert sol.isPalindrome1(x4) is False

    assert sol.isPalindrome2(x1) is True
    assert sol.isPalindrome2(x2) is False
    assert sol.isPalindrome2(x3) is True
    assert sol.isPalindrome2(x4) is False


if __name__ == '__main__':
    main()
