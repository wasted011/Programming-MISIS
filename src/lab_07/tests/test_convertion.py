import pytest, sys, os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.functions import *


def none_to_null(json_read: list | dict) -> list | dict:
    if isinstance(json_read, list):
        for element in json_read:
            for keys, values in element.items():
                if element[keys] == None:
                    element[keys] = ''
    elif isinstance(json_read, dict):
        for keys, values in json_read.items():
            if json_read[keys] == None:
                json_read[keys] = ''
    return json_read


json_to_csv_test =  [
        ("data/lab_05/json_to_csv.json", "data/lab_05/json_to_csv.csv")
    ]

csv_to_json_test = [
    ("data/lab_05/csv_to_json.csv", "data/lab_05/csv_to_json.json")
]

@pytest.mark.parametrize("source, expected", json_to_csv_test)

def test_json_to_csv(source, expected):
    func_source = json_load(Path(source))
    func_expected= read_csv_as_dict(Path(expected))
    
    assert none_to_null(func_source) == func_expected

@pytest.mark.parametrize("source, expected", csv_to_json_test)

def test_csv_to_json(source, expected):
    func_source = read_csv_as_dict(Path(source))
    func_expected= json_load(Path(expected))

    assert func_source == func_expected
