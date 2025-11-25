def transpose(mat: list[list[float | int]]) -> list[list]:
    rows, columns = len(mat), len(mat[0])
    clear_matrix = [[0] * rows for el in range(columns)]
    if len(mat) == 0:
        return mat
    for el in range(len(mat)):
        if len(mat[el - 1]) != len(mat[el]):
            return ValueError
    for r in range(rows):
        for c in range(columns):
            clear_matrix[c][r] = mat[r][c]
    return clear_matrix


print(transpose([[1, 2], [3, 4]]))
