import re
import csv
from pathlib import Path
from typing import Iterable, Sequence

#Arrays

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    flatten_mat = []
    for el in mat:
        if not isinstance(el, (list, tuple)):
            return TypeError
        flatten_mat += el
    return flatten_mat

#Matrices

def transpose(mat: list[list[float | int]]) -> list[list]:
    rows, columns = len(mat), len(mat[0])
    clear_matrix = [[0] * rows for el in range(columns)]
    if len(mat) == 0:
        return mat
    for el in range(len(mat)):
        if len(mat[el-1]) != len(mat[el]):
            return ValueError
    for r in range(rows):
        for c in range(columns):
            clear_matrix[c][r] = mat[r][c]
    return clear_matrix

def row_sums(mat: list[list[float | int]]) -> list[float]:
    rows, columns = len(mat), len(mat[0])
    sum_of_rows = []
    if rows == columns: 
        return "Матрица является квадратной, требуется прямоугольность (по усл.)"
    for index in range(len(mat)):
        sum_of_rows.append(sum(mat[index]))    
    return sum_of_rows

def col_sums(mat: list[list[float | int]]) -> list[float]:
    rows, columns = len(mat), len(mat[0])
    sample_of_matrix = transpose(mat)
    sum_of_columns = []
    if rows == columns:
        return "Матрица является квадратной, требуется прямоугольность (по усл.)"
    for el in sample_of_matrix:
        sum_of_columns.append(sum(el))
    return sum_of_columns

#Tokens

def normalize(text:str , *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = re.sub(r'[\t\r\n]', " ", text)
    text = re.sub(r'\s+', " ", text).strip()

    return text
def tokenize(text: str) -> list[str]:
    text = normalize(text)
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    unique_letters = list(set(tokens))
    new_dict = {}
    for el in unique_letters:
        new_dict.update({
            el: tokens.count(el)
        })
    return new_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    tuple_list = list(freq.items())
    tuple_list = sorted(tuple_list, key = lambda el: (-el[1], el[0]))
    return tuple_list[:n]

def script_01(text: str, n: int = 5):
    print(f"------------")
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(set(tokenize(normalize(text))))}")
    print("Топ-5:")
    text = top_n(count_freq(tokenize(normalize(text))))
    for el in text:
        print(f"{el[0]}: {el[1]}")
    return "------------"

# CSV/TXT

def read_text(path: str | Path, encoding: str = "utf-8-sig") -> str:
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError:
        return "Ошибка кодировки"
    except FileNotFoundError:
        return "Файл не найден"

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    for index in range(1, len(rows)):
        if len(rows[index-1]) != len(rows[index]):
            raise ValueError
    with p.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)