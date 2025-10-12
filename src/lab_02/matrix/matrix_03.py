def col_sums(mat: list[list[float | int]]) -> list[float]:
    rows, columns = len(mat), len(mat[0])
    sample_of_matrix = [[0] * rows for el in range (columns)]
    sum_of_columns = []
    for index in range(len(mat)):
        if len(mat[index-1]) != len(mat[index]):
            return ValueError
    if rows == columns:
        return "Матрица является квадратной, требуется прямоугольность (по усл.)"
    for r in range (rows):
        for c in range (columns):
            sample_of_matrix[c][r] = mat[r][c]
    for el in sample_of_matrix:
        sum_of_columns.append(sum(el))
    return sum_of_columns
print(col_sums([[1,2,3,4,5],[4,5,6,7,8]]))