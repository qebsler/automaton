from math import sqrt

def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def euclidian_distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    x1, y1 = a
    x2, y2 = b
    result = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 100
    return int(result) / 100
