import sys, argparse
sys.path.append('src')
from lib import *

parser = argparse.ArgumentParser(description='Анализ частот слов в тексте')
subparsers = parser.add_subparsers(dest = "command")

stats_parser = subparsers.add_parser("stats", help = "Статистика")
stats_parser.add_argument("--input", required=True)

cat_parser = subparsers.add_parser("inside", help = "Содержимое")
cat_parser.add_argument("--input", required=True)

args = parser.parse_args()

if args.command == "stats":
    if Path(args.input).stat().st_size != 0:
        print(script_01(read_text(Path(args.input))))
    else:
        print("Введенным текстом должен быть путь к файлу")
elif args.command == "inside":
    if Path(args.input).stat().st_size != 0:
        for element in read_text(Path(args.input)).split():
            print(element)
    else:
        print("Введным текстом должен быть путь к файлу")