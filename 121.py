from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            if prices[r] < prices[l]:
                l = r

            r += 1

        return max_profit


def main():
    sol = Solution()
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    assert sol.maxProfit(prices1) == 5
    assert sol.maxProfit(prices2) == 0


if __name__ == '__main__':
    main()
