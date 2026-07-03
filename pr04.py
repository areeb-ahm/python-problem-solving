# Write function flatten(nested_list). Takes list containing mix of numbers and nested lists (any depth). Returns single flat list.

def flatten(nested_list):
    new_list = []
    for item in nested_list:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list



print(flatten([1, [2, 3], [4, [5, 6, [7, 8]], 9]]))