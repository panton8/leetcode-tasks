from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
        all_keys = (ransom_dict + magazine_dict).keys()

        for key in all_keys:
            if magazine_dict.get(key, 0) < ransom_dict.get(key, 0):
                return False

        return True


def main():
    sol = Solution()
    ransomNote1 = "a"
    magazine1 = "b"
    ransomNote2 = "aa"
    magazine2 = "ab"
    ransomNote3 = "aa"
    magazine3 = "aab"

    assert sol.canConstruct(ransomNote1, magazine1) is False
    assert sol.canConstruct(ransomNote2, magazine2) is False
    assert sol.canConstruct(ransomNote3, magazine3) is True


if __name__ == '__main__':
    main()
