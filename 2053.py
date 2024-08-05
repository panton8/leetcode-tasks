from collections import Counter
from typing import List


class Solution:

    # T: O(n^2)  M: O(1)
    def kthDistinct1(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            is_unique = True
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    is_unique = False
                    break
            if is_unique:
                k -= 1
                if k == 0:
                    return arr[i]
        return ''

    # T: O(n) M: O(n)
    def kthDistinct2(self, arr: List[str], k: int) -> str:
        str_counter = Counter(arr)

        for i in range(len(arr)):
            if str_counter[arr[i]] == 1:
                k -= 1
                if k == 0:
                    return arr[i]

        return ''


def main():
    sol = Solution()

    arr1 = ['d', 'b', 'c', 'b', 'c', 'a']
    arr2 = ['aaa', 'aa', 'a']
    arr3 = ['a', 'b', 'a']

    assert sol.kthDistinct1(arr1, 2) == 'a'
    assert sol.kthDistinct1(arr2, 1) == 'aaa'
    assert sol.kthDistinct1(arr3, 3) == ''

    assert sol.kthDistinct2(arr1, 2) == 'a'
    assert sol.kthDistinct2(arr2, 1) == 'aaa'
    assert sol.kthDistinct2(arr3, 3) == ''


if __name__ == '__main__':
    main()
