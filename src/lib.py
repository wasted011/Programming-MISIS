import re
import csv, json
from pathlib import Path
from typing import Iterable, Sequence
from openpyxl import Workbook

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

def norm_token_freq(text: str) -> dict[str, int]:
    return count_freq(tokenize(normalize(text)))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    tuple_list = list(freq.items())
    tuple_list = sorted(tuple_list, key = lambda el: (-el[1], el[0]))
    return tuple_list[:n]

def script_01(text: str, n: int = 5):
    counter = 0
    print(f"------------")
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(set(tokenize(normalize(text))))}")
    print(f"Топ-{n}:")
    text = top_n(count_freq(tokenize(normalize(text))))
    for el in text:
        counter += 1
        if counter <= n:
            print(f"{el[0]}: {el[1]}")
    return "------------"

# FILES

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
    if Path(path).suffix == ".csv":
        p = Path(path)
        rows = list(rows)
        for index in range(1, len(rows)):
            if len(rows[index-1]) != len(rows[index]):
                raise ValueError
        with p.open("w", newline = '', encoding = "utf-8-sig") as f:
            w = csv.writer(f)
            if header is not None:
                w.writerow(header)
            for r in rows:
                w.writerow(r)
        return "Файл обработан корректно"
    elif Path(path).suffix != ".csv":
        return "Некорректное расширение"

def write_file(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if len(rows) == 0:
        raise FileNotFoundError
    with p.open("w", newline = None, encoding="utf-8-sig") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        w.writerow(rows)

def write_csv_lib(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    if Path(path).suffix == ".csv":
        p = Path(path)
        rows = list(rows)
        with p.open("w", newline = '', encoding = "utf-8-sig") as f:
            w = csv.writer(f)
            if header is not None:
                w.writerow(header)
            w.writerow(rows)
        return "Файл обработан корректно"
    elif Path(path).suffix != ".csv":
        return "Некорректное расширение"

def json_load(json_path: str | Path) -> None:
    json_path = Path(json_path)
    with json_path.open('r', newline='', encoding='utf-8') as file:
        data = json.load(file)
    return data

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    json_path = Path(json_path)
    try:
        values_of_csv = [values for keys, values in json_load(json_path).items()]
        keys_of_csv = [keys for keys, values in json_load(json_path).items()]
        write_csv_lib(values_of_csv, csv_path, keys_of_csv)
    except not json_path.exists():
        raise FileNotFoundError
    except (json_path.stat().st_size or csv_path.stat().st_size) == 0:
        return ValueError
    return 'Успешно'

def read_csv_as_dict(csv_path: str | Path) -> None:
    csv_path = Path(csv_path)
    with csv_path.open('r', newline='', encoding='utf-8-sig') as file:
        read_csv = csv.DictReader(file)
        for element in read_csv:
            return element

def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    json_path, csv_path = Path(json_path), Path(csv_path)
    dict_csv = read_csv_as_dict(csv_path)
    try:
        with json_path.open('w', newline='', encoding='utf-8-sig') as file:
            json.dump(dict_csv, file, ensure_ascii=False, indent=2)
    except not csv_path.exists():
        raise FileNotFoundError
    except (json_path.stat().st_size or csv_path.stat().st_size) == 0:
        return ValueError
    return 'Успешно'


def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    csv_path, xlsx_path = Path(csv_path), Path(xlsx_path)
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet_1"
        with csv_path.open(encoding='utf-8-sig') as file:
            for element in csv.reader(file):
                ws.append(element)
        wb.save(Path(xlsx_path))
        return "Успешно"
    except (csv_path.stat().st_size or xlsx_path.stat().st_size) == 0:
        raise ValueError
    except not csv_path.exists() or not xlsx_path.exist():
        raise FileNotFoundError