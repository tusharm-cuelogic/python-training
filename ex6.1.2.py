def flatten_list(a, result=None):
    """Flattens a nested list.

        >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result

nested_list = [ [1, 2, [3, 4] ], [5, 6], 7]
result = flatten_list(nested_list)
print result


# Recursion - 6.1.2. Example: Flatten a list
