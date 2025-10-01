matrix = [
    [1,2,3,4,5],
    [4,5,6,7,8]
]
rows, columns = len(matrix), len(matrix[0])
def transpose(matrix):
    newmatrix = [[0] * rows for el in range(columns)]
    for r in range(rows):
        for c in range(columns):
            newmatrix[c][r] = matrix[r][c]
    return newmatrix
new_matrix = transpose(matrix)
def column_sums(new_matrix, columns, rows):
    if columns != rows:
        result = []
        for el in range(columns):
            result.append(sum(new_matrix[el]))
    return result
print(column_sums(new_matrix, columns, rows))