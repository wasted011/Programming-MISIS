import sys, argparse
sys.path.append('src')
from lib import *

parser = argparse.ArgumentParser(description='Convertion')
subparsers = parser.add_subparsers(dest='command')

json_2_csv_parser = subparsers.add_parser('json2csv', help = 'Перевод из json в csv')
json_2_csv_parser.add_argument('--input', required=True)
json_2_csv_parser.add_argument('--output', required=True)

csv_2_json_parser = subparsers.add_parser('csv2json', help = 'Перевод из json в csv')
csv_2_json_parser.add_argument('--input', required=True)
csv_2_json_parser.add_argument('--output', required=True)

csv_2_xlsx = subparsers.add_parser('csv2xlsx', help = 'Перевод из csv в xlsx')
csv_2_xlsx.add_argument('--input', required=True)
csv_2_xlsx.add_argument('--output', required=True)

args = parser.parse_args()

if args.command == 'json2csv':
    if (Path(args.input).stat().st_size and Path(args.input).stat().st_size) != 0:
        print(json_to_csv(args.input, args.output))
    else:
        raise TypeError
elif args.command == 'csv2json':
    if (Path(args.input).stat().st_size and Path(args.input).stat().st_size) != 0:
        print(csv_to_json(args.input, args.output))
    else:
        raise TypeError
elif args.command == 'csv2xlsx':
    if (Path(args.input).stat().st_size and Path(args.input).stat().st_size) != 0:
        print(csv_to_xlsx(args.input, args.output))
    else:
        raise TypeError
