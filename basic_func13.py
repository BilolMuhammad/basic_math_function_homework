import math


def main(a):
    '''find the square root of a number and return it.

    Args:
        a (int): a number

    Returns:
        float: the absolute value.
    '''
    number = int(a)
    return math.sqrt(abs(number))


print(main(-196))
