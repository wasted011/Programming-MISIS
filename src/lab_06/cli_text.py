import argparse, sys
from pathlib import Path

sys.path.append('src')
from lib import *

def main():

    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")


    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help = "Ввод директории файла")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")


    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help = "Ввод директории файла")
    stats_parser.add_argument("--top", type=int, default=5, help = "Топ по введенному значению")

    args = parser.parse_args()

    if args.command == "cat":
        if Path(args.input).stat().st_size != 0:
            counter_of_word = 0
            if args.n:
                for element in read_text(Path(args.input)).split():
                    counter_of_word += 1
                    print(f"{counter_of_word}: {element}")
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
                part_01, part_02 = tokenize(normalize(text_line)), count_freq(part_01)
                print(part_02)
        else:
            raise FileNotFoundError
    else:
        parser.error("Неверный ввод комманды")
main()