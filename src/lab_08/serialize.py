import json, sys
sys.path.append("src")

from _functions_ import *
from pathlib import Path

def students_to_json(students: list[dict], json_path: str | Path):
    with Path(json_path).open('w', newline = '', encoding = 'utf-8-sig') as file:
        json.dump(students, file, indent = 2, ensure_ascii = False)
        return "Успешно"
    
def students_from_json(fio: str, json_path: str | Path):
    if is_not_empty(Path(json_path)):
        return json_load(Path(json_path))
    else:
        return "Пустой файл"
    
assert students_to_json([{"fio": "evgeny"}], "data/lab_08/students.json") == "Успешно"
assert students_from_json("Evgeny", "data/lab_08/students.json") == [{"fio": "evgeny"}]