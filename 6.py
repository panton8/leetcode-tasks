class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        up = True

        rows = {}
        index = 1

        for c in s:
            rows[index] = rows.get(index, '') + c

            if index == numRows:
                up = False

            if up:
                index += 1
            else:
                index -= 1

            if index == 1:
                up = True

        res = ''

        index = 1

        while index <= numRows:
            res += rows.get(index, '')
            index += 1

        return res


def main():
    sol = Solution()
    word1 = 'PAYPALISHIRING'
    word2 = 'PAYPALISHIRING'
    word3 = 'A'
    word4 = 'AB'

    assert sol.convert(word1, 3) == 'PAHNAPLSIIGYIR'
    assert sol.convert(word2, 4) == 'PINALSIGYAHRPI'
    assert sol.convert(word3, 1) == 'A'
    assert sol.convert(word4, 1) == 'AB'


if __name__ == '__main__':
    main()
