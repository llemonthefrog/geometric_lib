import math


def area(r):
    if r <= 0:
        raise ValueError()
    if type(r) not in [int, float]:
        raise TypeError()
    return math.pi * r * r


def perimeter(r):
    if r <= 0:
        raise ValueError()
    if type(r) not in [int, float]:
        raise TypeError()
    return 2 * math.pi * r
