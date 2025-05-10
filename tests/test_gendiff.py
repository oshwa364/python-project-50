from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsing import parse_files
from tests.test_data.results import (
    DIFF,
    DIFF_DEEP_JSON,
    DIFF_DEEP_PLAIN,
    DIFF_DEEP_STYLISH,
)

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

FILE1_DEEP_YAML, FILE2_DEEP_YAML = parse_files(
    'tests/test_data/file1_deep.yaml',
    'tests/test_data/file2_deep.yaml'
)


def test_gen():
    assert generate_diff(FILE1_JSON, FILE2_JSON) == DIFF
    assert generate_diff(FILE1_YAML, FILE2_YAML) == DIFF
    assert generate_diff(FILE1_DEEP_JSON, FILE2_DEEP_JSON) == DIFF_DEEP_STYLISH
    assert generate_diff(FILE1_DEEP_YAML, FILE2_DEEP_YAML) == DIFF_DEEP_STYLISH
    assert generate_diff(FILE1_DEEP_JSON, FILE2_DEEP_JSON, 'plain') == \
    DIFF_DEEP_PLAIN
    assert generate_diff(FILE1_DEEP_YAML, FILE2_DEEP_YAML, 'plain') == \
    DIFF_DEEP_PLAIN
    assert generate_diff(FILE1_DEEP_JSON, FILE2_DEEP_JSON, 'json') == \
    DIFF_DEEP_JSON