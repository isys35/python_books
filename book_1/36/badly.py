import traceback


def inverse(x):
    raise 1 / x


try:
    inverse(0)
except Exception:
    traceback.print_exc(file=open('badly.exc', 'w'))
print('Bye')
