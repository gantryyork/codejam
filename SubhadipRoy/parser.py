#!/usr/bin/env python3
import re
import argparse

filename = "./input.txt"
M_suffix = ['A', 'B', 'C']


def main(args):

    # Read in the file
    print(f"Reading {args.inputfile}")
    data = read_file(args.inputfile)

    # Modify data per requirements
    data = modify_data(data)

    # Display data
    display_data(data)


def read_file(filename):
    FILE = open(filename)  # Open filehandle for reading

    # Parse all data
    input_data = list()
    for line in FILE:

        data_search = re.match('.*__(.*)', line)

        if data_search:
            data = data_search.group(1).split()
            input_data.append(data)

    return input_data


def modify_data(data):

    modified_data = list()
    M_suffix_index = 0
    next_pin = ''
    last_pin = ''

    # Sort data.  Array of arrays is sorted on 1st columnn
    data.sort()

    for i in range(0, len(data) - 1):

        [pin, coef1, coef2, M] = data[i]

        if i+1 != len(data):
            next_pin = data[i+1][0]

        # modifying M
        if M in ['M2', 'M3', 'M4']:

            # If next pin is the same as current pin
            if (pin == next_pin) or (pin == last_pin):
                M = f"{M}_{M_suffix[M_suffix_index]}"

                # Cycle to front of M_suffix list
                if M_suffix_index == len(M_suffix) - 1:
                    M_suffix_index = 0
                else:
                    M_suffix_index += 1

            if pin != next_pin:
                M_suffix_index = 0

        # Modifying pin
        last_pin = pin
        pin = f"{pin}_probe"

        modified_data.append([pin, coef1, coef2, M])

    return modified_data


def display_data(data):

    for record in data:
        print(f"{record[0]} {record[1]} {record[2]} {record[3]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Subhadip's parsing tool"
    )
    parser.add_argument(
        '-i', '--inputfile',
        metavar='FILENAME',
        default="./input.txt",
        help="Input file to parse"
    )
    args = parser.parse_args()
    main(args)
