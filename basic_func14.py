from math import floor


def main(a, b):
    '''find the floor division of a and b and return it.

    Args:
        a (int): a number
        b (int): a number

    Returns:
        int: the result.
    '''
    return floor(int(a)/int(b))


print(main(7, 5))
