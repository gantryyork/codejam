#!/usr/bin/env python3

from enum import Enum


class Unit(Enum):

    KILOMETER = 'km'
    MILE = 'mi'


def main():

    unit = Unit.MILE

    if unit in list(Unit):
        print("we can convert this")
        convert_km(2, unit)


def convert_km(number, unit):

    scalar = {
        Unit.KILOMETER: 1,
        Unit.MILE: 3280.84
    }

    print(f"scalar={scalar[unit]}")


if __name__ == '__main__':
    main()
    exit()
