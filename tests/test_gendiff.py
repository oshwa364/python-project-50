from gendiff.scripts.gendiff import generate_diff
from tests.test_data.results import DIFF1

FILE1_JSON = 'tests/test_data/file1.json'
FILE2_JSON = 'tests/test_data/file2.json'

FILE1_YAML = 'tests/test_data/file1.yml'
FILE2_YAML = 'tests/test_data/file2.yml'


def test_gen():
    assert generate_diff(FILE1_JSON, FILE2_JSON) == DIFF1
    assert generate_diff(FILE1_YAML, FILE2_YAML) == DIFF1