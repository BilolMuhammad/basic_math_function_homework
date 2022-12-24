import math


def main(a, b):
    '''find the floor division of a and b and return it.

    Args:
        a (int): a number
        b (int): a number

    Returns:
        int: the result.
    '''
    return math.floor(a), math.floor(b)


print(main(3.4, 5.5))
