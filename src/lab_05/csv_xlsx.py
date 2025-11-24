import csv
from pathlib import Path
from openpyxl import Workbook 

from lib.functions import *


def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    csv_path, xlsx_path = Path(csv_path), Path(xlsx_path)
    if csv_path.suffix == ".csv" and xlsx_path.suffix == ".xlsx":
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Sheet_1"
            with csv_path.open(encoding='utf-8-sig') as file:
                for element in csv.reader(file):
                    ws.append(element)
            wb.save('data/lab_05/csv_to_xlsx.xlsx')
            return "Успешно"
        except (csv_path.stat().st_size or xlsx_path.stat().st_size) == 0:
            raise ValueError
        except not csv_path.exists() or not xlsx_path.exists():
            raise FileNotFoundError
    return "Неверный формат файла"

print(csv_to_xlsx('data/lab_05/csv_to_xlsx.csv', 'data/lab_05/csv_to_xlsx.xlsx'))
