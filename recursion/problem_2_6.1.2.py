def flatten_dict(a, result=None, p=""):
    """
        >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
        {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if result is None:
        result = {}

    for x, y in a.items():
        
        if isinstance(y, dict):
            result.update(flatten_dict(y, p = p + x + "."))
        else:
            result[p + x] = y 

    return result

nested_list = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
result = flatten_dict(nested_list)
print result


# Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
