from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        needed_diff = abs(alice - bob) // 2

        if alice > bob:
            needed_diff *= -1

        alice_set = set(aliceSizes)
        bob_set = set(bobSizes)

        for candy in alice_set:
            if (candy + needed_diff) in bob_set:
                return [candy, candy + needed_diff]


def main():
    sol = Solution()

    assert sol.fairCandySwap(aliceSizes=[35, 17, 4, 24, 10], bobSizes=[63, 21]) == [24, 21]
    assert sol.fairCandySwap(aliceSizes=[1, 1], bobSizes=[2, 2]) == [1, 2]
    assert sol.fairCandySwap(aliceSizes=[1, 2], bobSizes=[2, 3]) == [1, 2]
    assert sol.fairCandySwap(aliceSizes=[2], bobSizes=[1, 3]) == [2, 3]


if __name__ == '__main__':
    main()
