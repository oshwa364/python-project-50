from gendiff.scripts.parsing import parse_cli, parse_files


def format_value(val, depth):
    big_indent = '    ' * (depth + 1)
    indent = '   ' * depth
    if not isinstance(val, dict):
        if isinstance(val, bool):
            return 'true' if val else 'false'
        elif val is None:
            return 'null'
        else:
            return str(val)
    result = []
    for key, value in val.items():
        result.append(f'{big_indent}{key}: {format_value(value, depth + 1)}')
    return '{\n' + '\n'.join(result) + '\n' + indent + '}'


def stylish(diff: dict) -> str:
    replacer = ' '
    space_count = 4
    def inner(val, depth):
        big_indent = replacer * space_count * (depth + 1)
        indent_for_sigh = replacer * (space_count * (depth + 1) - 2)
        indent = replacer * space_count * depth
        result = []
        for key, value in val.items():
            match value['status']:
                case 'added':
                    result.append(f'{indent_for_sigh}+ {key}: {format_value(value['value'], depth + 1)}')
                case 'removed':
                    result.append(f'{indent_for_sigh}- {key}: {format_value(value['value'], depth + 1)}')
                case 'unchanged':
                    result.append(f'{big_indent}{key}: {format_value(value['value'], depth + 1)}')
                case 'changed':
                    result.append(f'{indent_for_sigh}- {key}: {format_value(value['old_value'], depth + 1)}')
                    result.append(f'{indent_for_sigh}+ {key}: {format_value(value['new_value'], depth + 1)}')
                case 'nested':
                    children = inner(value['children'], depth + 1)
                    result.append(f'{big_indent}{key}: {children}')
        return '{\n' + '\n'.join(result) + '\n' + indent + '}'

    return inner(dict(sorted(diff.items())), 0)


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
    result = stylish(diff)
    return result


def main():
    file_path1, file_path2 = parse_cli()
    file1, file2 = parse_files(file_path1, file_path2)
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
