from gendiff.plain import plain

file_a12 = {'= common': {'= setting1': 'Value 1', '+ follow': False, '+ setting4': 'blah blah', '+ setting5': {'? key5': 'value5'}, '- setting2': 200, '! setting3': [True, None], '= setting6': {'= key': 'value', '+ ops': 'vops', '= doge': {'! wow': ['', 'so much']}}}, '= group1': {'! baz': ['bas', 'bars'], '= foo': 'bar', '! nest': [{'? key': 'value'}, 'str']}, '- group2': {'? abc': 12345, '? deep': {'? id': 45}}, '+ group3': {'? deep': {'? id': {'? number': 45}}, '? fee': 100500}}


def test_stylish():
    f = open("tests/fixtures/my_answer_plain.txt", "w")
    f.write(plain(file_a12))
    f.close()
    file_answer = open("tests/fixtures/hexlet_answer_plain.txt", "r").read()
    answer = open("tests/fixtures/my_answer_plain.txt", "r").read()
    assert answer == file_answer
