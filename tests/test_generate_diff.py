from gendiff.generate_diff import generate_diff
import json

put1 = 'tests/fixtures/file1.json'
put2 = 'tests/fixtures/file2.json'

def test_generate_diff():
    f = open("tests/fixtures/file_answer.txt", "w")
    f.write(generate_diff(put1, put2))
    f.close()
    file_answer = open("tests/fixtures/file_answer.txt", "r").read()
    answer = open("tests/fixtures/answer.txt", "r").read()
    assert  file_answer == answer
