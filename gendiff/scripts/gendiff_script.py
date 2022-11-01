#!/usr/bin/env python
from ..generator import generate_diff
from ..args_gendiff import arguments


def main():
    args1, args2, format_name = arguments()
    diff = generate_diff(args1, args2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
