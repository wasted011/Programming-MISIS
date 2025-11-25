def row_sums(mat: list[list[float | int]]) -> list[float]:
    rows, columns = len(mat), len(mat[0])
    sum_of_rows = []
    for index in range(len(mat)):
        if len(mat[index - 1]) != len(mat[index]):
            return ValueError
    if rows == columns:
        return "Матрица является квадратной, требуется прямоугольность (по усл.)"
    for index in range(len(mat)):
        sum_of_rows.append(sum(mat[index]))
    return sum_of_rows


print(row_sums([[1, 2, 3], [4, 5, 6]]))
