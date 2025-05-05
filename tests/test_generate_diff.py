from gendiff.scripts.gendiff import generate_diff

DIFF = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_gen():
    assert generate_diff('file1.json', 'file2.json') == DIFF