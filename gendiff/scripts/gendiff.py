import argparse
import json


def parsing():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def change_booleans(coll: dict) -> dict:
    for key, value in coll.items():
        if isinstance(value, bool):
            coll[key] = 'true' if value else 'false'
    return coll


def generate_diff(file_path1: str, file_path2: str) -> str:
    result = '{\n'
    file1 = json.load(open(file_path1))
    file1 = change_booleans(file1)
    file2 = json.load(open(file_path2))
    file2 = change_booleans(file2)
    union_file = file1 | file2
    union_file = dict(sorted(union_file.items()))

    for key, value in union_file.items():
        if file1.get(key) == file2.get(key):
            result += f'    {key}: {value}\n'
        elif key in file1 and key in file2:
            result += f'  - {key}: {file1[key]}\n'
            result += f'  + {key}: {file2[key]}\n'
        elif key in file1:
            result += f'  - {key}: {file1[key]}\n'
        else:
            result += f'  + {key}: {value}\n'
    result += '}'
    return result


def main():
    file1_path1, file_path2 = parsing()
    print(generate_diff(file1_path1, file_path2))


if __name__ == '__main__':
    main()
