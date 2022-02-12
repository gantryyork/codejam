#!/usr/bin/env python3

import funcs

ips = [
    "10.30.28.10",
    "10.30.28.20",
    "10.30.28.30",
    "10.30.28.40",
]


def main():

    for ip in ips:
        print(f"Querying {ip}")

        try:
            query_something()
        except Exception as ex:
            print(f"main catches exception of type {type(ex)}")


def query_something():

    try:
        funcs.func1()
    except Exception as ex:
        raise ex


if __name__ == "__main__":
    main()
    exit()
