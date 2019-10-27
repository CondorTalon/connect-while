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

    def get_grid(self) - > List[List[chr]]:
        return self.grid 


    def token_drop(grid,length,width, token):
                grid[length][width] = token

    
    def vaild_location(grid, length):
        return grid [5][width] == 0 



