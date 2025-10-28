import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text_(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError:
        return "Ошибка кодировки"
    except FileNotFoundError:
        return "Файл не найден"
print(read_text_("C:/GitHub/Programming-MISIS/Programming-MISIS/data/lab_04/a.txt"))

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    if Path(path).suffix == ".csv":
        p = Path(path)
        rows = list(rows)
        if len(rows) == 0:
            raise FileNotFoundError
        for index in range(1, len(rows)):
            if len(rows[index-1]) != len(rows[index]):
                raise ValueError
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if header is not None:
                w.writerow(header)
            for r in rows:
                w.writerow(r)
        return "Файл обработан корректно"
    elif Path(path).suffix != ".csv":
        return "Некорректное расширение"
print(write_csv([("привет","count"),("привет","3")], "data/lab_04/check_01.csv"))
