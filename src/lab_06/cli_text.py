import argparse, sys
from pathlib import Path

sys.path.append('src')
from lib import *

def main():

    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")


    cat_parser = subparsers.add_parser("cat", help = "Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help = "Ввод директории файла")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")


    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help = "Ввод директории файла")
    stats_parser.add_argument("--top", dest = "top", required=False, type=int, help = "Топ по введенному значению")

    args = parser.parse_args()

    if args.command == "cat":
        if Path(args.input).stat().st_size != 0:
            if args.n:
                for index, element in enumerate(read_text(Path(args.input)).split()):
                    print(f"{index+1}: {element}")
            else:
                for element in read_text(Path(args.input)).split():
                    print(element)
        else:
            raise FileNotFoundError
    elif args.command == "stats":
        if Path(args.input).stat().st_size != 0:
            text_line = read_text(Path(args.input))
            if args.top:
                print(script_01(text_line, args.top))
            else:
                part_01, part_02 = normalize(text_line),  tokenize(part_01)
                part_03 = count_freq(part_02)
                for keys, values in part_03.items():
                    print(f"{keys}: {values}")
        else:
            raise FileNotFoundError

main()