def product(x, n):
    """
    product to multiply 2 numbers recursively using + and - operators only.

        >>> product(2, 3)
        6
        >>> product(4, 2)
        8
    """
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return x + product(x, n-1)


result = product(4, 3)
print result

# Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.