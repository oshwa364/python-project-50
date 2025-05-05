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
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    return first_file, second_file


def main():
    parsing()


if __name__ == '__main__':
    main()