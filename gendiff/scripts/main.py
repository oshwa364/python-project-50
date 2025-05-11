from gendiff.cli import parse_cli
from gendiff.scripts.gendiff import generate_diff


def main():
    file_path1, file_path2, format_name = parse_cli()
    print(generate_diff(file_path1, file_path2, format_name))


if __name__ == '__main__':
    main()
