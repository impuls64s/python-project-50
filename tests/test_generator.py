from gendiff.generator import generate_diff


def test_generate_diff_stylish():
    result1 = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    file_answer1 = open("tests/fixtures/hexlet_answer_stylish.txt", "r").read()
    assert result1 == file_answer1
    
    result3 = generate_diff('tests/fixtures/json-file1.json', 'tests/fixtures/json-file2.json')
    file_answer3 = open("tests/fixtures/hexlet_answer2_stylish.txt", "r").read()
    assert result3 == file_answer3


def test_generate_diff_plain():
    result2 = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain')
    file_answer2 = open("tests/fixtures/hexlet_answer_plain.txt", "r").read()
    assert result2 == file_answer2


def test_generate_diff_json():
    result4 = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')
    file_answer4 = open("tests/fixtures/hexlet_answer_json.json", "r").read()
    assert result4 == file_answer4