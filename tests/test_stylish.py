from gendiff.formater.stylish import stylish


text = {'= common': {'= setting1': 'Value 1', '- setting2': 200, '- setting3': True, '+ setting3': None, '= setting6': {'= key': 'value', '= doge': {'- wow': '', '+ wow': 'so much'}, '+ ops': 'vops'}, '+ follow': False, '+ setting4': 'blah blah', '+ setting5': {'= key5': 'value5'}}, '= group1': {'- baz': 'bas', '+ baz': 'bars', '= foo': 'bar', '- nest': {'= key': 'value'}, '+ nest': 'str'}, '- group2': {'= abc': 12345, '= deep': {'= id': 45}}, '+ group3': {'= deep': {'= id': {'= number': 45}}, '= fee': 100500}}
text2 = {'= host': 'hexlet.io', '+ verbose': True, '- timeout': 50, '+ timeout': 20, '- proxy': '123.234.53.22', '- follow': False}

def test_stylish():
    f = open("tests/fixtures/my_answer_stylish.txt", "w")
    f.write(stylish(text))
    f.close()
    file_answer = open("tests/fixtures/hexlet_answer_stylish.txt", "r").read()
    answer = open("tests/fixtures/my_answer_stylish.txt", "r").read()
    assert answer == file_answer

    f = open("tests/fixtures/my_answer2_stylish.txt", "w")
    f.write(stylish(text2))
    f.close()
    file_answer2 = open("tests/fixtures/hexlet_answer2_stylish.txt", "r").read()
    answer2 = open("tests/fixtures/my_answer2_stylish.txt", "r").read()
    assert answer2 == file_answer2