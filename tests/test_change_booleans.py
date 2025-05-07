from gendiff.scripts.parsing import change_booleans

TEST_DICT = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io",
    "my_value": {
        "other_value": False
    }
}

RES_DICT = {
    "timeout": 20,
    "verbose": 'true',
    "host": "hexlet.io",
    "my_value": {
        "other_value": 'false'
        }
}


def test_change_booleans():
    assert change_booleans(TEST_DICT) == RES_DICT