"""Import 'functools' module of python"""
import functools


def count_calls(func):
    """Decorator for counting for function call"""

    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        """wrapper function for counting function call"""

        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


def memoize(func):
    """Decorator to Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_memoize(arg):
        """wrapper function for memoization"""

        memoize_key = arg
        if memoize_key not in wrapper_memoize.memoize:
            wrapper_memoize.memoize[memoize_key] = func(arg)

        return wrapper_memoize.memoize[memoize_key]

    wrapper_memoize.memoize = dict()
    return wrapper_memoize


@memoize
@count_calls
def fibonacci(n):
    """Nth fibonacci member"""

    print("Computing fibonacci({})".format(n))
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(40)
