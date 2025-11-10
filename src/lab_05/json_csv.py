import json, csv, sys, pathlib
sys.path.append('src')
from lib import *

def json_load(json_path: str | Path) -> None:
    json_path = Path(json_path)
    with json_path.open('r', newline='', encoding='utf-8-sig') as file:
        data = json.load(file)
    return data

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    json_path = Path(json_path)
    all_in_once_dict = {}
    try:
        for element in json_load(json_path):
            all_in_once_dict.update(element)
        keys = [keys for keys, values in all_in_once_dict.items()]
        values = [values for keys, values in all_in_once_dict.items()]
        write_csv_lib(values, csv_path, keys)
        return "Успешно"
    except not json_path.exists():
        raise FileNotFoundError
    except (json_path.stat().st_size or csv_path.stat().st_size) == 0:
        return ValueError
print(json_to_csv('data/lab_05/json_to_csv.json', 'data/lab_05/json_to_csv.csv'))

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
            return "Успешно"
    except not csv_path.exists():
        raise FileNotFoundError
    except (json_path.stat().st_size or csv_path.stat().st_size) == 0:
        return ValueError
print(csv_to_json('data/lab_05/csv_to_json.csv', 'data/lab_05/csv_to_json.json'))