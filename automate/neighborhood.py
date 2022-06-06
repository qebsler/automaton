from automate.distance import euclidian_distance, manhattan_distance

def is_inside(a: tuple[int, int], dimensions: tuple[int, int]) -> bool:
    x, y = a
    height, width = dimensions
    return 0 <= x < width and 0 <= y < height


def radial_neighborhood(a: tuple[int, int], radius: int, dimensions: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = a
    neighborhood = []
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if is_inside((i, j), dimensions) and euclidian_distance((i, j), a) <= radius:
                neighborhood.append((i, j))

    return neighborhood


def moore_neighborhood(a: tuple[int, int], radius: int, dimensions: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = a
    neighborhood = []
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if is_inside((i, j), dimensions):
                neighborhood.append((i, j))

    return neighborhood


def von_neumann_neighborhood(a: tuple[int, int], radius: int, dimensions: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = a
    neighborhood = []
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if is_inside((i, j), dimensions) and manhattan_distance((i, j), a) <= radius:
                neighborhood.append((i, j))

    return neighborhood
