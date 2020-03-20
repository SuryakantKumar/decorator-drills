"""Import 'math', 'time' and 'functools' modules of python"""
import math
import time
import functools


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        """Wrapper function"""
        start_time = time.perf_counter()   # Return float value of performance time

        value = func(*args, **kwargs)

        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(
            f"time taken by {func.__name__!r} of {args[0]} is : {run_time:.8f}")

        return value
    return wrapper_timer


@timer
def sqrt(x):
    """function for finding square root of a number"""
    return math.sqrt(x)


@timer
def square(x):
    """function for finding square of a number"""
    return x * x


sqrt(10000)
square(10000)
