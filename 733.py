from typing import List
from collections import namedtuple


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        curr_color = image[sr][sc]
        image[sr][sc] = color
        self.change_color(image, sr, sc, curr_color, color)

        return image

    def change_color(self, image, sr, sc, curr_color, new_color):
        if self.is_pixel_exist(sr - 1, sc, image) and image[sr-1][sc] == curr_color:
            image[sr-1][sc] = new_color
            self.change_color(image, sr - 1, sc, curr_color, new_color)
        if self.is_pixel_exist(sr + 1, sc, image) and image[sr+1][sc] == curr_color:
            image[sr+1][sc] = new_color
            self.change_color(image, sr + 1, sc, curr_color, new_color)
        if self.is_pixel_exist(sr, sc - 1, image) and image[sr][sc-1] == curr_color:
            image[sr][sc-1] = new_color
            self.change_color(image, sr, sc - 1, curr_color, new_color)
        if self.is_pixel_exist(sr, sc + 1, image) and image[sr][sc+1] == curr_color:
            image[sr][sc+1] = new_color
            self.change_color(image, sr, sc + 1, curr_color, new_color)

    def is_pixel_exist(self, sr, sc, image):
        return 0 <= sr < len(image) and 0 <= sc < len(image[sr])


def main():
    sol = Solution()
    TestData = namedtuple('TestData', ['image', 'sr', 'sc', 'color'])
    test1 = TestData(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
    test2 = TestData(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)

    assert sol.floodFill(test1.image, test1.sr, test1.sc, test1.color) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert sol.floodFill(test2.image, test2.sr, test2.sc, test2.color) == [[0, 0, 0], [0, 0, 0]]


if __name__ == "__main__":
    main()
