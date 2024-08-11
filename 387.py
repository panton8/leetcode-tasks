class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1


def main():
    sol = Solution()

    assert sol.firstUniqChar('leetcode') == 0
    assert sol.firstUniqChar('loveleetcode') == 2
    assert sol.firstUniqChar('aabb') == -1


if __name__ == '__main__':
    main()
