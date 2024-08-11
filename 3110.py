class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))

        return score


def main():
    sol = Solution()

    assert sol.scoreOfString('hello') == 13
    assert sol.scoreOfString('zaz') == 50


if __name__ == '__main__':
    main()
