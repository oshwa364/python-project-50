from gendiff.formatters.format_stylish import format_value

NESTED_DICTIONARY = '''{
        a: 1
        b: {
            c: 2
        }
    }'''


def test_format_value_stylish():
    assert format_value('', 0) == ''
    assert format_value(False, 0) == 'false'
    assert format_value(None, 1) == 'null'
    assert format_value('just string', 2) == 'just string'
    assert format_value([1, True, None], 3) == '[1, True, None]'
    assert format_value({'a': 1, 2: 'b'}, 0) == '{\n    a: 1\n    2: b\n}'
    assert format_value({'a': 1, 'b': {'c': 2}}, 1) == NESTED_DICTIONARY
