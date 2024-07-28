class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = len(a) - len(b)

        if diff > 0:
            for i in range(abs(diff)):
                b = '0' + b
        elif diff < 0:
            for i in range(abs(diff)):
                a = '0' + a

        additional = False
        res = ''

        for i in range(len(a)-1, -1, -1):
            answ = self.combination_res(a[i], b[i], additional)
            res = answ[0] + res
            additional = answ[1]
        if additional:
            return '1' + res

        return res

    def combination_res(self, a, b, addition):
        if a == '0' and b == '0':
            if not addition:
                return '0', addition
            return '1', False
        elif a == '1' and b == '0' or a == '0' and b == '1':
            if not addition:
                return '1', addition
            return '0', addition

        elif a == '1' and b == '1':
            if not addition:
                return '0', True
            return '1', addition


def main():
    sol = Solution()
    a1 = "11"
    b1 = "1"
    a2 = "1010"
    b2 = "1011"

    assert sol.addBinary(a1, b1) == '100'
    assert sol.addBinary(a2, b2) == '10101'


if __name__ == '__main__':
    main()
