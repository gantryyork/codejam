#!/usr/bin/env python3
import re

filename = "./input.txt"
M_suffix = ['A', 'B', 'C']


def main():

    FILE = open(filename)  # Open filehandle for reading

    # Parse all data
    parsed_data = list()
    for line in FILE:

        data_search = re.match('.*__(.*)', line)

        if data_search:
            data = data_search.group(1).split()
            parsed_data.append(data)

    # Modify data
    parsed_data.sort()  # sorts parsed_data by first col
    last_pin = ''
    M_suffix_index = 0

    for data in parsed_data:

        [pin, num1, num2, M] = data
        #print(f"{pin} {num1} {num2} '{M}'")

        # Adding M suffix if necessary

        if pin == last_pin:
            if M in ['M2', 'M3', 'M4']:
                M = M + "_" + M_suffix[M_suffix_index]

                # if you run out of M suffixes, start over
                if M_suffix_index == len(M_suffix):
                    M_suffix_index = 0
                else:
                    M_suffix_index += 1

        else:
            M_suffix_index = 0

        last_pin = pin

        # Add _probe to pin
        pin = pin + "_probe"

        print(f"{pin} {num1} {num2} {M}")


if __name__ == "__main__":
    main()
    exit()
