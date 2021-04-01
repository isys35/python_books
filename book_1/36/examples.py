import sys


class MyError(IndexError):
    pass


def oops():
    raise MyError


def oops2():
    try:
        oops()
    except MyError:
        print(sys.exc_info()[0:2])


if __name__ == '__main__':
    oops2()
