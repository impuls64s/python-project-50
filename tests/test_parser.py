<<<<<<< HEAD
from gendiff.parser import why_format , parsing
=======
from gendiff.parser import why_format, parsing
>>>>>>> 700e474e68ee5ce1ffcfc688827d876b58635546


def test_why_format():
    assert why_format('file1.json', 'file2.json') == 'json'
    assert why_format('file1.json', 'file2.yaml') == 'wrong format'
    assert why_format('file1.yml', 'file2.json') == 'wrong format'
    assert why_format('file1.yml', 'file2.yml') == '.yml'
    assert why_format('file1.yaml', 'file2.yml') == 'yaml'
    assert why_format('file1.yml', 'file2.yaml') == 'yaml'
    assert why_format('file1.yml', 'file2.json') == 'wrong format'
    assert why_format('file1.ymll', 'file2.json') == 'wrong format'


def test_parsing():
    two_dict = ({'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
               {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'})
    assert parsing('tests/fixtures/json-file1.json', 'tests/fixtures/json-file2.json') == two_dict
    assert parsing('tests/fixtures/yml-file1.yml', 'tests/fixtures/yml-file2.yml') == two_dict
    assert parsing('tests/fixtures/json-file1.yyyml', 'tests/fixtures/json-file2.yml') == 'wrong format'
