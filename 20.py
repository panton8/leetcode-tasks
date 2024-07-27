class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        prnts_dict = {'(': ')', '[': ']', '{': '}'}
        for prnt in s:
            if prnt in prnts_dict:
                stack.append(prnt)
                continue
            if stack and prnts_dict[stack[-1]] == prnt:
                stack.pop()
                continue
            return False

        return len(stack) == 0


def main():
    s_1 = "()"
    s_2 = "()[]{}"
    s_3 = "(]"

    assert Solution().isValid(s_1) is True
    assert Solution().isValid(s_2) is True
    assert Solution().isValid(s_3) is False


if __name__ == '__main__':
    main()
