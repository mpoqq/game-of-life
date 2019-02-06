import numpy as np


def num_neighbours(x, y, grid):
    num = 0
    x_max = grid.shape[0]
    y_max = grid.shape[1]
    if x - 1 >= 0 and y - 1 >= 0 and grid[x - 1, y - 1] > 0:
        num += 1
    if x - 1 >= 0 and grid[x - 1, y] > 0:
        num += 1
    if x - 1 >= 0 and y + 1 < y_max and grid[x - 1, y + 1] > 0:
        num += 1
    if y - 1 >= 0 and grid[x, y - 1] > 0:
        num += 1
    if y + 1 < y_max and grid[x, y + 1] > 0:
        num += 1
    if x + 1 < x_max and y - 1 >= 0 and grid[x + 1, y - 1] > 0:
        num += 1
    if x + 1 < x_max and grid[x + 1, y] > 0:
        num += 1
    if x + 1 < x_max and y + 1 < y_max and grid[x + 1, y + 1] > 0:
        num += 1
    return num


def compute_next_generation(grid):
    new_grid = np.copy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            num = num_neighbours(x, y, grid)
            # rule death by overcrowding and loneliness
            if grid[x, y] and not 2 <= num <= 3:
                new_grid[x, y] = 0
            # birth
            elif num == 3:
                new_grid[x, y] += 1
            # survival
            elif grid[x, y] and num == 2:
                new_grid[x, y] += 1
            # max life
            if new_grid[x, y] > 5:
                new_grid[x, y] = 5
    return new_grid
