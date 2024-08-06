from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for key in t_counter:
            if t_counter[key] - s_counter.get(key, 0) != 0:
                return key


def main():
    sol = Solution()

    s1 = "abcd"
    t1 = "abcde"
    s2 = ''
    t2 = 'y'

    assert sol.findTheDifference(s1, t1) == 'e'
    assert sol.findTheDifference(s2, t2) == 'y'


if __name__ == '__main__':
    main()

