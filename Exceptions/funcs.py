import random


def func1():

    try:
        request_something()
    except Exception as ex:
        raise ex


def request_something():

    num = random.randint(0, 100)
    print(num)
    if 0 < num and num < 10:
        raise OverflowError
    if 10 < num and num < 30:
        raise NameError
    if 30 < num and num < 55:
        raise RuntimeError

    assert num < 60
