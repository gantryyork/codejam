#!/usr/bin/python3 

#example1.py -r A -x 1234 -r B

import argparse

import pprint
pp = pprint.PrettyPrinter(indent=4)


def main(args):

    print( args.resource)
    print( args.xid )

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r', '--resource',
        action='append',
    )
    parser.add_argument(
        '-x', '--xid',
        action='store'
    )
    args = parser.parse_args()
    main(args)
