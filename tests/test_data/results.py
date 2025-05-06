FILE1_DICT = {
    'host': 'hexlet.io', 'timeout': 50, 
    'proxy': "123.234.53.22", 'follow': 'false'
}

FILE2_DICT = {
    'timeout': 20, 'verbose': 'true', 'host': 'hexlet.io'
}


UNION1 = {
'follow': 'false', 
'host': 'hexlet.io', 
'proxy': "123.234.53.22", 
'timeout': 20, 
'verbose': 'true'
}

DIFF1 = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''