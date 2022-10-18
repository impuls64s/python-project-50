import json


def generate_diff(url1, url2):
    file1 = json.load(open(url1))
    file2 = json.load(open(url2))
    result = {}
    for k, v in file1.items():
        if k in file2 and v == file2[k]:
            result['=' + k] = v
        elif k in file2 and v != file2[k]:
            result['-' + k] = v
            result['+' + k] = file2[k]
        else:
            result['-' + k] = v
    for k, v in file2.items():
        if k not in file1:
            result['+' + k] = v
    sorted_tuple = dict(sorted(result.items(), key=lambda x: x[0][1]))
    result_str = '''{'''
    for k, v in sorted_tuple.items():
        result_str += f'\n  {k}: {v}'
    result_str += '\n}\n'

    result_finish = (result_str.replace('False', 'false')
                               .replace('True', 'true').replace('=', '  ')
                               .replace('=', ' ').replace("'", '')
                               .replace('-', '- ').replace('+', '+ '))
    return result_finish
