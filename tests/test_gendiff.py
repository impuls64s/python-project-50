from gendiff.scripts.gendiff import main


def test_main():
    result = '''usage: gendiff.py [-h] [-f FORMAT] first_file second_file
gendiff.py: error: the following arguments are required: first_file, second_file'''
    assert main() == print(result)
