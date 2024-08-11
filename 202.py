class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)

            n = self.squares_sum(n)

            if n == 1:
                return True

        return False

    def squares_sum(self, num: int) -> int:
        sq_sum = 0

        while num != 0:
            sq_sum += (num % 10)**2
            num //= 10

        return sq_sum


def main():
    sol = Solution()

    assert sol.isHappy(19) is True
    assert sol.isHappy(2) is False
    assert sol.isHappy(1) is True
    assert sol.isHappy(8) is False


if __name__ == '__main__':
    main()