def flatten(mat: list[list | tuple]) -> list:
    flatten_mat = []
    for el in mat:
        if not isinstance(el, (list, tuple)):
            return TypeError
        flatten_mat += el
    return flatten_mat


print(flatten([[1, 2], (3, 4, 5)]))
