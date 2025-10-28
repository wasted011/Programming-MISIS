import sys
sys.path.append("C:\GitHub\Programming-MISIS\Programming-MISIS\src")
from lib import *
def script_02(text: str):
    tok_norm = tokenize(normalize(text))
    freq_top = top_n(count_freq(tok_norm))
    write_csv(freq_top, "data/lab_04/report_02.csv")
    return script_01(text)
print(script_02(read_text("C:\GitHub\Programming-MISIS\Programming-MISIS\data\lab_04\input.txt")))