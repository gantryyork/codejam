#!/usr/bin/env python3
import re

filename = "./input.txt"


def main():

    FILE = open(filename)

    parsed_data = list()
    for line in FILE:

        data_search = re.match('.*__(.*)', line)

        if data_search:
            data = data_search.group(1).split()
            print(data)
            parsed_data.append(data)

    parsed_data.sort()
    print(parsed_data)


if __name__ == "__main__":
    main()
    exit()
