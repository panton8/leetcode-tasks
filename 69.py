class Solution:

    # T: O(n^0.5)
    def mySqrt1(self, x: int) -> int:
        for i in range(x + 1):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1

    # T: O(log(n))
    def mySqrt2(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            sqrt = (r + l) // 2
            if sqrt*sqrt == x:
                return sqrt
            if sqrt*sqrt > x:
                r = sqrt - 1
            else:
                l = sqrt + 1
                res = sqrt

        return res


def main():
    sol = Solution()

    assert sol.mySqrt1(8) == 2
    assert sol.mySqrt2(8) == 2
    assert sol.mySqrt1(4) == 2
    assert sol.mySqrt1(4) == 2
    assert sol.mySqrt1(0) == 0
    assert sol.mySqrt1(0) == 0
    assert sol.mySqrt1(54) == 7
    assert sol.mySqrt1(54) == 7


if __name__ == '__main__':
    main()
