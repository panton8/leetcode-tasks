class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_type_counter = {}

        for stone in stones:
            stones_type_counter[stone] = stones_type_counter.get(stone, 0) + 1

        jewels_count = 0

        for jewel in jewels:
            jewels_count += stones_type_counter.get(jewel, 0)

        return jewels_count


def main():
    sol = Solution()

    assert sol.numJewelsInStones('aA', 'aAAbbbb') == 3
    assert sol.numJewelsInStones('qw', 'qD') == 1
    assert sol.numJewelsInStones('z', 'ZZ') == 0


if __name__ == '__main__':
    main()
