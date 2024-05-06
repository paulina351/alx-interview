#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
        A function that returns the perimeter of the island
        described in grid.

        grid is a list of integers:
        0 represents water
        1 represents land

        The grid is completely surrounded by water
        There is only one island
        The island doesn't have lakes
    """
    is_perimeter = 0
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == 1:
                if a == 0 or grid[a - 1][b] == 0:
                    is_perimeter += 1
                if b == 0 or grid[a][b - 1] == 0:
                    is_perimeter += 1
                if a == len(grid) - 1 or grid[a + 1][b] == 0:
                    is_perimeter += 1
                if b == len(grid[a]) - 1 or grid[a][b + 1] == 0:
                    is_perimeter += 1
    return (is_perimeter)
