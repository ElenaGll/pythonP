from collections import defaultdict
from functools import wraps


def memoizing(value):

    def wrapper(func):
        d = defaultdict()

        @wraps(func)
        def inner(arg):
            if arg not in d:
                if len(d) < value:
                    result = func(arg)
                    d[arg] = result
                    return result
                else:
                    first_key = list(d.keys())[0]
                    del d[first_key]
                    result = func(arg)
                    d[arg] = result
                    return result
            else:
                return d[arg]

        return inner
    return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10
