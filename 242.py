class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1

        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        return s_dict == t_dict


def main():
    sol = Solution()
    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"

    assert sol.isAnagram(s1, t1) is True
    assert sol.isAnagram(s2, t2) is False


if __name__ == '__main__':
    main()
