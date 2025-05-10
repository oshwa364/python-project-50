from gendiff.formatters.format_json import format_json
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_stylish import format_stylish


def make_diff(file1, file2):
    diff = dict()
    keys = sorted(file1 | file2)

    for key in keys:
        if key not in file1:
            diff[key] = {
                'status': 'added',
                'value': file2[key]
            }
        elif key not in file2:
            diff[key] = {
                'status': 'removed',
                'value': file1[key]
            }
        else:
            value1, value2 = file1[key], file2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                nested = make_diff(value1, value2)
                diff[key] = {
                    'status': 'nested',
                    'children': nested
                }
            elif value1 == value2:
                diff[key] = {
                    'status': 'unchanged',
                    'value': value1
                }
            else:
                diff[key] = {
                    'status': 'changed',
                    'old_value': value1,
                    'new_value': value2
                }
    return diff


def generate_diff(file1, file2, format_name='stylish') -> str:
    diff = make_diff(file1, file2)
    match format_name:
        case 'stylish':
            result = format_stylish(diff)
        case 'plain':
            result = format_plain(diff)
        case 'json':
            result = format_json(diff)
    return result
