def exp(x, n):
    """
    Computes the result of x raised to the power of n.

        >>> exp(2, 3)
        8
        >>> exp(3, 2)
        9
    """
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)


result = exp(2, 10)
print result

# Recursion - 6.1.1. Example: Computing Exponent
# Recursive call to itself.