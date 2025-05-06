from gendiff.scripts.gendiff import generate_diff
from tests.test_data.results import DIFF1

FILE1 = 'tests/test_data/file1.json'
FILE2 = 'tests/test_data/file2.json'


def test_gen():
    assert generate_diff(FILE1, FILE2) == DIFF1