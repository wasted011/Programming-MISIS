import sys, argparse
sys.path.append('src')
from lib import *

def is_not_empty(input_argument: str, output_argument: str) -> bool:
    path_input_argument, path_output_argument = Path(input_argument), Path(output_argument)
    if path_input_argument.stat().st_size and path_output_argument.stat().st_size != 0:
        return True
    return False

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
        if is_not_empty(args.input, args.output):
            print(json_to_csv(args.input, args.output))
        else:
            raise TypeError
    elif args.command == 'csv2json':
        if is_not_empty(args.input, args.output):
            print(csv_to_json(args.input, args.output))
        else:
            raise TypeError
    elif args.command == 'csv2xlsx':
        if is_not_empty(args.input, args.output):
            print(csv_to_xlsx(args.input, args.output))
        else:
            raise TypeError

main()
