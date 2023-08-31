#!/usr/bin/python3
"""
island perimeter
"""
def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    grid is a list of list of integers:List[list[int]]
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t
    connected to the water surrounding the island).
    """
    row_length = len(grid)
    column_length = len(grid[0])

    perimeter = 0
    connections = 0

    # iterate through each row and column
    for x in range(0, row_length):
        for y in range(0, column_length):
            # find out when we have a   1
            if grid[x][y] == 1:
                perimeter += 4

                # CHECKING IF OUR ROW IS AT THE TOP
                if x != 0 and grid[x - 1][y] == 1:
                    connections += 1
                if y != 0 and grid[x][y - 1] == 1:
                    connections += 1
    return perimeter - (connections * 2)
