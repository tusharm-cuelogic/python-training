def unflatten_dict(a, result=None):
    """
        >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
        {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    """
    if result is None:
        result = {}

    for key, value in a.items():

        if "." in key:
            parent, child = key.split(".", 1)
            if parent in result.keys():
                result[parent].update(unflatten_dict({child:value}))
            else:
                result.update({parent: unflatten_dict({child:value})})

        else:
           result.update({key:value})

    return result

nested_list = {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
result = unflatten_dict(nested_list)
print result


# Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.
