import json, csv, sys, os
from pathlib import *

sys.path.append('src')
from _lib_ import *

def json_load(json_path: str | Path):
    json_path = Path(json_path)
    if json_path.suffix == ".json":
        with json_path.open('r', newline='', encoding='utf-8-sig') as file:
            data = json.load(file)
        return data
    return "Неверный формат файла"

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    json_path, csv_path = Path(json_path), Path(csv_path)
    with json_path.open('r', newline = '', encoding = 'utf-8-sig') as file:
        data = json_load(json_path)
        if isinstance(data, list):
            csv_header = [element for element in data[0]]
            data = list(data)
        elif isinstance(data, dict):
            csv_header = data.keys()
            data = [data]
    with csv_path.open('w', newline = '', encoding = 'utf-8-sig') as file:
        csv_file = csv.DictWriter(file, fieldnames=csv_header)
        csv_file.writeheader(), csv_file.writerows(data)
        return "Успешно"

print(json_to_csv('data/lab_05/json_to_csv.json', 'data/lab_05/json_to_csv.csv'))

def read_csv_as_dict(csv_path: str | Path) -> None:
    csv_path = Path(csv_path)
    if csv_path.suffix == ".csv":
        clean_list = []
        with csv_path.open('r', newline='', encoding='utf-8-sig') as file:
            read_csv = csv.DictReader(file)
            for element in read_csv:
                clean_list.append(element)
        return clean_list
    return "Неверный формат файла"

def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    json_path, csv_path = Path(json_path), Path(csv_path)
    dict_csv = read_csv_as_dict(csv_path)
    try:
        with json_path.open('w', newline='', encoding='utf-8-sig') as file:
            json.dump(dict_csv, file, indent = 2, ensure_ascii = False)
            return "Успешно"
    except not csv_path.exists():
        raise FileNotFoundError
    except (json_path.stat().st_size or csv_path.stat().st_size) == 0:
        raise ValueError
print(csv_to_json('data/lab_05/csv_to_json.csv', 'data/lab_05/csv_to_json.json'))