#!/usr/bin/python3
"""
moduel with function that returns perimeter of island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    rows = len(grid)
    if grid != []:
        columns = len(grid[0])

    sum = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                if (i - 1) == -1 or grid[i - 1][j] == 0:
                    sum += 1
                if (i + 1) == rows or grid[i + 1][j] == 0:
                    sum += 1
                if (j - 1) == -1 or grid[i][j - 1] == 0:
                    sum += 1
                if (j + 1) == columns or grid[i][j + 1] == 0:
                    sum += 1
    return sum
