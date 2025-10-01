matrix = [
    [1,2,3,4],
    [3],
]
rows, columns = len(matrix), len(matrix[0])
def row_sums(matrix, rows, columns):
    if rows != columns:
        result = []
        for el in range(rows):
            result.append(sum(matrix[el]))
        return result
print(row_sums(matrix, rows, columns))