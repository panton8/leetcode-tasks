class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for index, c in enumerate(s):
            if not s_dict.get(c):
                s_dict[c] = [index]
            else:
                s_dict[c].append(index)

        for index, c in enumerate(t):
            if not t_dict.get(c):
                t_dict[c] = [index]
            else:
                t_dict[c].append(index)

        if len(s_dict) != len(t_dict):
            return False

        for pair in zip(s_dict.values(), t_dict.values()):
            if pair[0] != pair[1]:
                return False

        return True


def main():
    sol = Solution()

    assert sol.isIsomorphic('egg', 'add') is True
    assert sol.isIsomorphic('foo', 'bar') is False
    assert sol.isIsomorphic('paper', 'title') is True


if __name__ == '__main__':
    main()
