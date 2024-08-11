class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for c in address:
            if c == '.':
                res = res + '[.]'
            else:
                res = res + c

        return res


def main():
    sol = Solution()

    assert sol.defangIPaddr('1.1.1.1') == '1[.]1[.]1[.]1'
    assert sol.defangIPaddr('255.100.50.0') == '255[.]100[.]50[.]0'


if __name__ == '__main__':
    main()
