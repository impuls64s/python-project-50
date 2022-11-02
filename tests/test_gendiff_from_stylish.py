from gendiff.gendiff_from_stylish import data_from_stylish


file1 = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
file2 = {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
file3 = {'= common': {'= setting1': 'Value 1', '- setting2': 200, '- setting3': True, '+ setting3': None, '= setting6': {'= key': 'value', '= doge': {'- wow': '', '+ wow': 'so much'}, '+ ops': 'vops'}, '+ follow': False, '+ setting4': 'blah blah', '+ setting5': {'= key5': 'value5'}}, '= group1': {'- baz': 'bas', '+ baz': 'bars', '= foo': 'bar', '- nest': {'= key': 'value'}, '+ nest': 'str'}, '- group2': {'= abc': 12345, '= deep': {'= id': 45}}, '+ group3': {'= deep': {'= id': {'= number': 45}}, '= fee': 100500}}

file4 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
file5 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
file6 = {'= host': 'hexlet.io', '+ verbose': True, '- timeout': 50, '+ timeout': 20, '- proxy': '123.234.53.22', '- follow': False}


def test_data_from_stylish():
    var1 = data_from_stylish(file1, file2)
    assert var1 == file3
    var2 = data_from_stylish(file4, file5)
    assert var2 == file6
