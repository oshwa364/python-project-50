import json
import os

import yaml


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

    return file1, file2
