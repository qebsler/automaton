from random import randint

from automate.display import show_CA
from automate.neighborhood import von_neumann_neighborhood

grid = [[0 for _ in range(50)] for _ in range(50)]


def anim(grid: list[list[int]], step: int):
    x = randint(0, 49)
    y = randint(0, 49)
    new_grid = grid

    for cell in von_neumann_neighborhood((x, y), randint(1, 10), (50, 50)):
        a, b = cell
        new_grid[a][b] = step

    return new_grid


show_CA(grid, anim)
