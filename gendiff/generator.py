from .gendiff_all import data_from_gendiff
from .formater.stylish import stylish
from .formater.plain import plain
from .formater.json import json_f
from .parser import parsing


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = parsing(file_path1)
    dict2 = parsing(file_path2)
    gendiff_result = data_from_gendiff(dict1, dict2)
    if format_name == 'stylish':
        return stylish(gendiff_result)
    elif format_name == 'plain':
        return plain(gendiff_result)
    elif format_name == 'json':
        return json_f(gendiff_result)
