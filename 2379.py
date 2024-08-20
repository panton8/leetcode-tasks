class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = 0
        b_count = 0
        min_recolor = float("inf")
        l = 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                w_count += 1
            else:
                b_count += 1

            if r - l + 1 == k:
                min_recolor = min(min_recolor, w_count)
                if blocks[l] == 'W':
                    w_count -= 1
                else:
                    b_count -= 1
                l += 1

        return min_recolor


def main():
    sol = Solution()
    s1 = 'WBBWWBBWBW'
    s2 = 'WBWBBBW'
    s3 = 'BBBWB'

    assert sol.minimumRecolors(s1, 7) == 3
    assert sol.minimumRecolors(s2, 2) == 0
    assert sol.minimumRecolors(s3, 5) == 1


if __name__ == '__main__':
    main()
