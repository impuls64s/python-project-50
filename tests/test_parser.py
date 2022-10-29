from gendiff.parser import parsing


def test_parsing():
    result1 = parsing('tests/fixtures/file123.json')
    assert result1 ==  {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    result2 = parsing('tests/fixtures/file123.yml')
    assert result2 == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    result3 = parsing('tests/fixtures/file123.yyamll')
    assert result3 == 'wrong format'