from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = ''
        l, r = 0, len(letters) - 1

        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                ans = letters[mid]
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return ans or letters[0]


def main():
    sol = Solution()

    letters1 = ["c", "f", "j"]
    target1 = "a"
    letters2 = ["c", "f", "j"]
    target2 = "c"
    letters3 = ["x", "x", "y", "y"]
    target3 = "z"


    assert sol.nextGreatestLetter(letters1, target1) == "c"
    assert sol.nextGreatestLetter(letters2, target2) == "f"
    assert sol.nextGreatestLetter(letters3, target3) == "x"


if __name__ == "__main__":
    main()