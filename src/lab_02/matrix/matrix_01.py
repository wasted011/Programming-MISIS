matrix = [
    [1,2,3],
    [4,5,6],
    [3]
]
rows, columns = len(matrix), len(matrix[0])
def transpose(matrix, rows, columns):
    newmatrix = [[0] * rows for el in range(columns)]
    if len(matrix) == 0:
        return matrix
    for el in range(len(matrix)):
        if len(matrix[el-1]) != len(matrix[el]):
            return ValueError
    else:
        for r in range(rows):
            for c in range(columns):
                newmatrix[c][r] = matrix[r][c]
    return newmatrix
print(transpose(matrix, rows, columns))