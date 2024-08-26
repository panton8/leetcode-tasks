from typing import List


class Solution:
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        last_index = None
        possible_places = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)

        for i in range(1, len(flowerbed) - 1):

            if flowerbed[i - 1:i + 2] == [0, 0, 0] and last_index != i - 1:
                possible_places += 1
                last_index = i

        return possible_places >= n

    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        free_place = 0 if flowerbed[0] else 1

        for flower in flowerbed:
            if flower:
                n -= abs((free_place-1)) // 2
                free_place = 0
            else:
                free_place += 1

        n -= free_place // 2

        return n <= 0


def main():
    sol = Solution()

    assert sol.canPlaceFlowers1([1, 0, 0, 0, 1], 1) is True
    assert sol.canPlaceFlowers1([1, 0, 0, 0, 1], 2) is False
    assert sol.canPlaceFlowers1([0, 0, 1, 0, 1], 1) is True
    assert sol.canPlaceFlowers1([1, 0, 0, 0, 1, 0, 0], 2) is True

    assert sol.canPlaceFlowers2([1, 0, 0, 0, 1], 1) is True
    assert sol.canPlaceFlowers2([1, 0, 0, 0, 1], 2) is False
    assert sol.canPlaceFlowers2([0, 0, 1, 0, 1], 1) is True
    assert sol.canPlaceFlowers2([1, 0, 0, 0, 1, 0, 0], 2) is True
    assert sol.canPlaceFlowers2([1, 0, 0, 0, 0, 1], 2) is False


if __name__ == '__main__':
    main()
