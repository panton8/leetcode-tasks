def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_bad = n

        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                first_bad = mid
                l = mid + 1
            else:
                r = mid - 1

        return first_bad
