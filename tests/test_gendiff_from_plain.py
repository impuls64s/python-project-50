from gendiff.gendiff_from_plain import data_from_plain

file1 = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
file2 = {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
file_a12 = {'= common': {'= setting1': 'Value 1', '+ follow': False, '+ setting4': 'blah blah', '+ setting5': {'? key5': 'value5'}, '- setting2': 200, '! setting3': [True, None], '= setting6': {'= key': 'value', '+ ops': 'vops', '= doge': {'! wow': ['', 'so much']}}}, '= group1': {'! baz': ['bas', 'bars'], '= foo': 'bar', '! nest': [{'? key': 'value'}, 'str']}, '- group2': {'? abc': 12345, '? deep': {'? id': 45}}, '+ group3': {'? deep': {'? id': {'? number': 45}}, '? fee': 100500}}

file4 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
file5 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
file_a45 = {'= host': 'hexlet.io', '+ verbose': True, '! timeout': [50, 20], '- proxy': '123.234.53.22', '- follow': False}

def test_data_from_plain():
    var1 = data_from_plain(file1, file2)
    assert var1 == file_a12
    var2 = data_from_plain(file4, file5)
    assert var2 == file_a45