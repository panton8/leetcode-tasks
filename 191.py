class Solution:

    # M:O(n) T: O(n)
    def hammingWeight1(self, n: int) -> int:
        binary_repr = []

        while n > 0:
            binary_repr.append(n % 2)
            n //= 2

        return binary_repr.count(1)

    def hammingWeight2(self, n: int) -> int:
        binary_bit_count = 0

        while n > 0:
            if n % 2:
                binary_bit_count += 1
            n //= 2

        return binary_bit_count


def main():
    sol = Solution()

    assert sol.hammingWeight1(5) == 2
    assert sol.hammingWeight1(4) == 1

    assert sol.hammingWeight2(5) == 2
    assert sol.hammingWeight2(4) == 1


if __name__ == '__main__':
    main()