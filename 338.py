from typing import List


class Solution:
    # T: O(nlogn)
    def countBits1(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.count_bits_for_num(i))

        return result

    def count_bits_for_num(self, n: int) -> int:
        binary_bit_count = 0

        while n > 0:
            if n % 2:
                binary_bit_count += 1
            n //= 2

        return binary_bit_count

    # T: O(n)
    def countBits2(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            result[i] = 1 + result[i - offset]

        return result


def main():
    sol = Solution()

    assert sol.countBits1(1) == [0, 1]
    assert sol.countBits1(5) == [0, 1, 1, 2, 1, 2]
    assert sol.countBits1(0) == [0]

    assert sol.countBits2(1) == [0, 1]
    assert sol.countBits2(5) == [0, 1, 1, 2, 1, 2]
    assert sol.countBits2(0) == [0]


if __name__ == '__main__':
    main()
