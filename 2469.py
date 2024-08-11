from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K = celsius + 273.15
        F = celsius * 1.8 + 32.00
        return [K, F]


def main():
    sol = Solution()

    assert sol.convertTemperature(36.50) == [309.65000, 97.70000]
    assert sol.convertTemperature(122.11) == [395.26000, 251.79800]


if __name__ == '__main__':
    main()
