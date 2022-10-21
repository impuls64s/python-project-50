from gendiff.generate_diff import generate_diff


dict1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
dict2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

def test_generate_diff():
    result = generate_diff(dict1, dict2)
    f = open("tests/fixtures/func_answer.txt", "w")
    f.write(result)
    f.close()
    file_answer = open("tests/fixtures/true_answer.txt", "r").read()
    answer = open("tests/fixtures/func_answer.txt", "r").read()
    assert  file_answer == answer
