from typing import List


class QuadlineGrid:
    col: int
    row: int
    grid: List[List[str]]   # can change to string if needed

    def __init__(self) -> None:
        self.row = 6
        self.col = 7
        self.grid = []

        for y in range(self.row):
            temp_grid = []
            for x in range(self.col):
                temp_grid.append(" ")
            self.grid.append(temp_grid)

    def get_grid(self) -> List[List[str]]:
        return self.grid

    def drop_token(self, length, width, token):
        self.grid[length][width] = token

    def valid_location(self, col) -> bool:
        return self.grid[0][col] == " "
