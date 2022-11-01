#!/usr/bin/env python

from ..gendiff_from_stylish import data_from_stylish
from ..gendiff_from_plain import data_from_plain
from ..parser import parsing
from ..stylish import stylish
from ..plain import plain
from ..args_gendiff import arguments


def main():
    args1, args2, format_name = arguments()
    dict1 = parsing(args1)
    dict2 = parsing(args2)
    if format_name == 'stylish':
        result_from_stylish = data_from_stylish(dict1, dict2)
        res_stylish = stylish(result_from_stylish)
        print(res_stylish)
    if format_name == 'plain':
        result_from_plain = data_from_plain(dict1, dict2)
        res_plain = plain(result_from_plain)
        print(res_plain)


if __name__ == '__main__':
    main()
