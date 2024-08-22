class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        bin_num = ''

        while num:
            if num % 2 == 0:
                bin_num = '0' + bin_num
            else:
                bin_num = '1' + bin_num
            num //= 2

        new_num = ''
        for b in bin_num:
            if b == '1':
                new_num = new_num + '0'
            else:
                new_num = new_num + '1'

        res = 0
        for index, b in enumerate(reversed(new_num)):
            if b == '1':
                res += 2**index

        return res


def main():
    sol = Solution()

    assert sol.findComplement(5) == 2
    assert sol.findComplement(1) == 0
    assert sol.findComplement(3) == 0
    assert sol.findComplement(0) == 1
    assert sol.findComplement(10) == 5


if __name__ == '__main__':
    main()
