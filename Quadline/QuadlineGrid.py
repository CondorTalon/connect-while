from typing import List


class QuadlineGrid:
    length: int
    width: int
    grid: List[List[chr]]   # can change to string if needed

    def __init__(self) -> None:
        self.length = 7
        self.width = 6
        self.grid = []

        x = 0
        y = 0
        for y in range(self.width):
            temp_grid = []
            for x in range(self.length):
                temp_grid.append(" ")
            self.grid.append(temp_grid)

    def get_grid(self):
        return self.grid    # should be changed to return later




