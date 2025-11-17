import argparse, sys
from pathlib import Path

sys.path.append('src')
from lib import *

def is_not_empty(input_argument: str | Path) -> bool:
    path_input_argument = Path(input_argument)
    if path_input_argument.stat().st_size != 0:
        return True
    return False

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
        if is_not_empty(args.input):
            if args.n:
                for index, element in enumerate(read_text(Path(args.input)).split()):
                    print(f"{index+1}: {element}")
            else:
                for element in read_text(Path(args.input)).split():
                    print(element)
        else:
            raise FileNotFoundError
    elif args.command == "stats":
        if is_not_empty(args.input):
            text_line = read_text(Path(args.input))
            if args.top:
                print(script_01(text_line, args.top))
            else:
                argument = norm_token_freq(text_line)
                for keys, values in argument.items():
                    print(f"{keys}: {values}")
        else:
            raise FileNotFoundError

main()