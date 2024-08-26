class Solution:
    def mergeAlternately1(self, word1: str, word2: str) -> str:
        res = ''

        word1_len = len(word1)
        word2_len = len(word2)

        min_len = min(word1_len, word2_len)
        last = 0

        for i in range(min_len):
            merge = word1[i] + word2[i]
            res = res + merge
            last += 1

        if word1_len > word2_len:
            res += word1[last:]
        if word2_len > word1_len:
            res += word2[last:]

        return res

    def mergeAlternately2(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        total_len = word1_len + word2_len
        res = ''

        for i in range(total_len):
            if i < word1_len:
                res += word1[i]
            if i < word2_len:
                res += word2[i]

        return res
