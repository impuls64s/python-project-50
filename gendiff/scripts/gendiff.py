import argparse
from ..generate_diff import generate_diff


def gendiff():
    desc = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=(desc))
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f FORMAT', '--format FORMAT',
                        help='set format of output', action="store_true")
    args = parser.parse_args()
    args1, args2 = args.first_file, args.second_file
    print(generate_diff(args1, args2))


def main():
    gendiff()


if __name__ == '__main__':
    main()


