def area(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        raise ValueError()
    if (type(a) in [str, bool]) or (type(b) in [str, bool]) or (type(c) in [str, bool]):
        raise TypeError()
    return (a + b + c) / 2


def perimeter(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        raise ValueError()
    if (type(a) in [str, bool]) or (type(b) in [str, bool]) or (type(c) in [str, bool]):
        raise TypeError()
    return a + b + c
