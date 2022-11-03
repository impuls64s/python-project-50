from gendiff.formater.stylish import stylish


text = {'= common': {'+ follow': False, '= setting1': 'Value 1', '- setting2': 200, '! setting3': [True, None], '+ setting4': 'blah blah', '+ setting5': {'= key5': 'value5'}, '= setting6': {'= doge': {'! wow': ['', 'so much']}, '= key': 'value', '+ ops': 'vops'}}, '= group1': {'! baz': ['bas', 'bars'], '= foo': 'bar', '! nest': [{'= key': 'value'}, 'str']}, '- group2': {'= abc': 12345, '= deep': {'= id': 45}}, '+ group3': {'= deep': {'= id': {'= number': 45}}, '= fee': 100500}}
text2 = {'- follow': False, '= host': 'hexlet.io', '- proxy': '123.234.53.22', '! timeout': [50, 20], '+ verbose': True}


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
