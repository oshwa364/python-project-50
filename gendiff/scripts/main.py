from gendiff.cli import parse_cli
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsing import parse_files


def main():
    file_path1, file_path2, format_name = parse_cli()
    file1, file2 = parse_files(file_path1, file_path2)
    print(generate_diff(file1, file2, format_name))


if __name__ == '__main__':
    main()
