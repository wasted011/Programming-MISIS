import sys, argparse, os

sys.path.append('src')
from _lib_ import *


def main():
    
    parser = argparse.ArgumentParser(description='Convertion')
    subparsers = parser.add_subparsers(dest='command')

    json_2_csv_parser = subparsers.add_parser('json2csv', help = 'Перевод из json в csv')
    json_2_csv_parser.add_argument('--input', required=True, help = "Ввод директории входного файла")
    json_2_csv_parser.add_argument('--output', required=True, help = "Ввод директории файла выхода")

    csv_2_json_parser = subparsers.add_parser('csv2json', help = 'Перевод из json в csv')
    csv_2_json_parser.add_argument('--input', required=True,  help = "Ввод директории входного файла")
    csv_2_json_parser.add_argument('--output', required=True,  help = "Ввод директории файла выхода")

    csv_2_xlsx = subparsers.add_parser('csv2xlsx', help = 'Перевод из csv в xlsx')
    csv_2_xlsx.add_argument('--input', required=True,  help = "Ввод директории входного файла")
    csv_2_xlsx.add_argument('--output', required=True,  help = "Ввод директории файла выхода")

    args = parser.parse_args()

    if args.command == 'json2csv':
        print(json_to_csv(args.input, args.output))
    elif args.command == 'csv2json':
        print(csv_to_json(args.input, args.output))
    elif args.command == 'csv2xlsx':
        print(csv_to_xlsx(args.input, args.output))

main()
