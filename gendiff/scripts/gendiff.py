from gendiff.scripts.parsing import parse_CLI, parse_files


def generate_diff(file_path1: str, file_path2: str) -> str:
    result = '{\n'
    
    file1, file2, union_file = parse_files(file_path1, file_path2)

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
    file1_path1, file_path2 = parse_CLI()
    print(generate_diff(file1_path1, file_path2))


if __name__ == '__main__':
    main()
