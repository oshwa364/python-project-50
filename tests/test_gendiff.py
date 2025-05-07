from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsing import parse_files
from tests.test_data.results import DIFF, DIFF_DEEP

FILE1_JSON, FILE2_JSON = parse_files(
    'tests/test_data/file1.json',
    'tests/test_data/file2.json'
 )

FILE1_YAML, FILE2_YAML = parse_files(
    'tests/test_data/file1.yml',
    'tests/test_data/file2.yml'
)

FILE1_DEEP_JSON, FILE2_DEEP_JSON = parse_files(
    'tests/test_data/file1_deep.json',
    'tests/test_data/file2_deep.json'
)


def test_gen():
    assert generate_diff(FILE1_JSON, FILE2_JSON) == DIFF
    assert generate_diff(FILE1_YAML, FILE2_YAML) == DIFF
    assert generate_diff(FILE1_DEEP_JSON, FILE2_DEEP_JSON) == DIFF_DEEP