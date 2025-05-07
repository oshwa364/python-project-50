import argparse
import json
import os

import yaml


def parse_cli():
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
        elif isinstance(value, dict):
            change_booleans(coll[key])
    return coll


def parse_files(file_path1, file_path2):
    _, ext = os.path.splitext(file_path1)
    if ext == '.json':
        with open(file_path1, 'r') as f1:
            file1 = json.load(f1)
        with open(file_path2, 'r') as f2:
            file2 = json.load(f2)
    else:
        with open(file_path1, 'r') as f1:
            file1 = yaml.safe_load(f1)

        with open(file_path2, 'r') as f2:
            file2 = yaml.safe_load(f2)

    file1 = change_booleans(file1)
    file2 = change_booleans(file2)
    return file1, file2
