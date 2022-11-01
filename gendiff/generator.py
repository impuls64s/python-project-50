from .gendiff_from_stylish import data_from_stylish
from .gendiff_from_plain import data_from_plain
from .formater.stylish import stylish
from .formater.plain import plain
from .formater.json import json_f


def generate_diff(dict1, dict2, format_name='stylish'):
    if format_name == 'stylish':
        result_from_stylish = data_from_stylish(dict1, dict2)
        res_stylish = stylish(result_from_stylish)
        return res_stylish
    if format_name == 'plain':
        result_from_plain = data_from_plain(dict1, dict2)
        res_plain = plain(result_from_plain)
        return res_plain
    if format_name == 'json':
        result_from_json = data_from_stylish(dict1, dict2)
        res_json = json_f(result_from_json)
        return res_json
