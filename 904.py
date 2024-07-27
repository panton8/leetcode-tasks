class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        collectable_fruits = set()
        max_amount = 0
        curr_amount = 0

        for index, fruit in enumerate(fruits):
            if fruit not in collectable_fruits and len(collectable_fruits) < 2:
                collectable_fruits.add(fruit)
                curr_amount += 1
            elif fruit in collectable_fruits:
                curr_amount += 1
            else:
                curr_amount = 2
                collectable_fruits = {fruits[index-1], fruit}
                for i in range(index-1, 0, -1):
                    if fruits[i] == fruits[i-1]:
                        curr_amount += 1
                    else:
                        break
            max_amount = max(curr_amount, max_amount)

        return max_amount


def main():
    fruits_1 = [1, 2, 3]
    fruits_2 = [1, 2, 3, 3]
    fruits_3 = [1, 2, 3, 1, 1]
    fruits_4 = [1, 2, 1]
    fruits_5 = [1, 2, 3, 2, 2]
    fruits_6 = [1, 2]
    fruits_7 = [1, 1, 1, 1, 1, 1, 1, 2]
    fruits_8 = [0, 1, 6, 6, 4, 4, 6]

    sol = Solution()
    assert sol.totalFruit(fruits_1) == 2
    assert sol.totalFruit(fruits_2) == 3
    assert sol.totalFruit(fruits_3) == 3
    assert sol.totalFruit(fruits_4) == 3
    assert sol.totalFruit(fruits_5) == 4
    assert sol.totalFruit(fruits_6) == 2
    assert sol.totalFruit(fruits_7) == 8
    assert sol.totalFruit(fruits_8) == 5


if __name__ == '__main__':
    main()
