import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.functions import *

normalize_test = [
    ("ПрИвЕт\nМИр\t", "привет мир"),
    ("ёжик, Ёлка", "ежик, елка"),
    ("Hello\r\nWorld", "hello world"),
    ("  двойные   пробелы  ", "двойные пробелы"),
    ]

tokenize_test = [
    ("привет мир", ["привет", "мир"]),
    ("ежик елка", ["ежик", "елка"]),
    ("hello world", ["hello", "world"]),
    ("двойные пробелы", ["двойные", "пробелы"])
]

count_freq_test = [
    (["привет", "мир"], {"привет": 1, "мир": 1}),
    (["ежик", "елка"], {"ежик": 1, "елка": 1}),
    (["hello", "world"], {"hello": 1, "world": 1}),
    (["двойные", "пробелы"], {"двойные": 1, "пробелы": 1})
]

top_n_test = [
    ({"привет": 1, "мир": 1}, [("мир", 1), ("привет", 1)]),
    ({"ежик": 1, "елка": 1}, [("ежик", 1), ("елка", 1)]),
    ({"hello": 1, "world": 1}, [("hello", 1), ("world", 1)]),
    ({"двойные": 1, "пробелы": 1}, [("двойные", 1), ("пробелы", 1)])
]

@pytest.mark.parametrize("source, expected", normalize_test)

def test_normalize_basic(source, expected):
    assert normalize(source) == expected

@pytest.mark.parametrize("source, expected", tokenize_test)

def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected

@pytest.mark.parametrize("source, expected", count_freq_test)

def test_count_freq_basic(source, expected):
    assert count_freq(source) == expected

@pytest.mark.parametrize("source, expected", top_n_test)

def test_top_n_basic(source, expected):
    assert top_n(source) == expected