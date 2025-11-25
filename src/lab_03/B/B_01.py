import sys

sys.path.append("C:\GitHub\Programming-MISIS\Programming-MISIS\src")
from lib import *


def script(text: str, n: int = 5):
    print(f"------------")
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(set(tokenize(normalize(text))))}")
    print("Топ-5:")
    text = top_n(count_freq(tokenize(normalize(text))))
    for el in text:
        print(f"{el[0]}: {el[1]}")
    return "------------"


print(script("привет привет привет привет мир мир мир мир"))
