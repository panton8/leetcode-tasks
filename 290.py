class Solution:
    def wordPattern1(self, pattern: str, s: str) -> bool:
        symbols = set(pattern)
        pattern_letters = []

        for p in pattern:
            if p in symbols:
                pattern_letters.append(p)
                symbols.remove(p)

        s_dict = {}
        s_pattern = ''
        s = s.split(' ')
        letters_size = len(pattern_letters)
        current = -1

        for c in s:
            if c not in s_dict:
                current += 1
                if current >= letters_size:
                    return False
                s_dict[c] = pattern_letters[current]
            s_pattern = s_pattern + s_dict[c]

        return s_pattern == pattern

    def wordPattern2(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        word_to_char = {}
        char_to_word = {}

        for w, c in zip(words, pattern):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False

            word_to_char[w] = c
            char_to_word[c] = w

        return True


def main():
    sol = Solution()

    assert sol.wordPattern1(pattern="deadbeef", s="d e a d b e e f") is True
    assert sol.wordPattern1(pattern="aaaa", s="dog cat cat dog") is False
    assert sol.wordPattern1(pattern='e', s='qwerty')

    assert sol.wordPattern2(pattern="deadbeef", s="d e a d b e e f") is True
    assert sol.wordPattern2(pattern="aaaa", s="dog cat cat dog") is False
    assert sol.wordPattern2(pattern='e', s='qwerty')


if __name__ == '__main__':
    main()
