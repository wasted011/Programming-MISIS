import sys
sys.path.append("C:\GitHub\Programming-MISIS\Programming-MISIS\src")
from lib import *
def script_02(text: str):
    write_csv(top_n(count_freq(tokenize(normalize(text)))), "data/report.csv")
    return script_01(text)
print(script_02(read_text("C:\GitHub\Programming-MISIS\Programming-MISIS\data\input.txt")))