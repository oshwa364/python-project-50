from gendiff.scripts.parsing import parse_files
from tests.test_data.results import FILE1_DICT, FILE2_DICT

FILE1_JSON = 'tests/test_data/file1.json'
FILE2_JSON = 'tests/test_data/file2.json'

FILE1_YAML = 'tests/test_data/file1.yml'
FILE2_YAML = 'tests/test_data/file2.yml'


def test_parse_files():
    assert parse_files(FILE1_JSON, FILE2_JSON) == \
    (FILE1_DICT, FILE2_DICT)
    assert parse_files(FILE1_YAML, FILE2_YAML) == \
    (FILE1_DICT, FILE2_DICT)