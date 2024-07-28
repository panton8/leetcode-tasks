from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.check_stair(n, 0)

    @lru_cache
    def check_stair(self, target, stair):
        if stair == target:
            return 1
        if stair > target:
            return 0
        return self.check_stair(target, stair+1) + self.check_stair(target, stair+2)


def main():
    sol = Solution()
    n1 = 2
    n2 = 3

    assert sol.climbStairs(n1) == 2
    assert sol.climbStairs(n2) == 3


if __name__ == '__main__':
    main()
    