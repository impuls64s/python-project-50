from gendiff.formater.json import json_f


file_a12 = {'= common': {'+ follow': False, '= setting1': 'Value 1', '- setting2': 200, '! setting3': [True, None], '+ setting4': 'blah blah', '+ setting5': {'= key5': 'value5'}, '= setting6': {'= doge': {'! wow': ['', 'so much']}, '= key': 'value', '+ ops': 'vops'}}, '= group1': {'! baz': ['bas', 'bars'], '= foo': 'bar', '! nest': [{'= key': 'value'}, 'str']}, '- group2': {'= abc': 12345, '= deep': {'= id': 45}}, '+ group3': {'= deep': {'= id': {'= number': 45}}, '= fee': 100500}}


def test_json_f():
    f = open("tests/fixtures/my_answer_json.json", "w")
    f.write(json_f(file_a12))
    f.close()
    file_answer = open("tests/fixtures/hexlet_answer_json.json", "r").read()
    answer = open("tests/fixtures/my_answer_json.json", "r").read()
    assert answer == file_answer
