REPLACER = ' '
SPACE_COUNT = 4


def format_value(val, depth):
    big_indent = REPLACER * SPACE_COUNT * (depth + 1)
    indent = REPLACER * SPACE_COUNT * depth
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


def format_stylish(diff: dict) -> str:

    def inner(val, depth):
        big_indent = REPLACER * SPACE_COUNT * (depth + 1)
        sigh_indent = REPLACER * (SPACE_COUNT * (depth + 1) - 2)
        indent = REPLACER * SPACE_COUNT * depth
        result = []
        for key, value in val.items():
            match value['status']:
                case 'added':
                    result.append(f'{sigh_indent}+ {key}: {format_value(value['value'], depth + 1)}')  # noqa: E501
                case 'removed':
                    result.append(f'{sigh_indent}- {key}: {format_value(value['value'], depth + 1)}')  # noqa: E501
                case 'unchanged':
                    result.append(f'{big_indent}{key}: {format_value(value['value'], depth + 1)}')  # noqa: E501
                case 'changed':
                    result.append(f'{sigh_indent}- {key}: {format_value(value['old_value'], depth + 1)}')  # noqa: E501
                    result.append(f'{sigh_indent}+ {key}: {format_value(value['new_value'], depth + 1)}')  # noqa: E501
                case 'nested':
                    children = inner(value['children'], depth + 1)
                    result.append(f'{big_indent}{key}: {children}')
        return '{\n' + '\n'.join(result) + '\n' + indent + '}'

    return inner(dict(sorted(diff.items())), 0)