#!/usr/bin/env python
from ..gendiff import generate_diff
from ..args_gendiff import arguments
from ..parser import parsing


def main():
    args1, args2, format_name = arguments()
    file_path1 = parsing(args1)
    file_path2 = parsing(args2)
    diff = generate_diff(file_path1, file_path2, format_name)
    print(diff)


if __name__ == '__main__':
    main()