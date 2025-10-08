
def area(a):
    if a <= 0:
        raise ValueError()
    if type(a) in [str, bool]:
        raise TypeError()
    return a * a


def perimeter(a):
    if a <= 0:
        raise ValueError()
    if type(a) in [str, bool]:
        raise TypeError()
    return 4 * a
