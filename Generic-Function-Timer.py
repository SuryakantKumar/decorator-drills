"""Import 'time' and 'functools' module of python"""
import time
import functools


def generic_timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        """wrapper function"""
        start_timer = time.perf_counter()       # Return float value of performance time

        value = func(*args, **kwargs)

        end_timer = time.perf_counter()

        run_time = end_timer - start_timer

        print(f"time taken by {func.__name__!r} is : {run_time:.8f}")
        return value

    return wrapper_timer


@generic_timer
def add(x, y):
    """function for addition of two parameters"""
    return x + y


@generic_timer
def add3(x, y, z):
    """function for addition of three parameters"""
    return x + y + z


@generic_timer
def add_any(*args):
    """function for addition of any parameters"""
    return sum(args)


@generic_timer
def abs_add_any(*args, **kwargs):
    """function for addition of any parameters with abs value as kwargs"""
    total = sum(args)
    if kwargs.get('abs') is True:
        return abs(total)
    return total


add(5, 10)
add3(5, 10, 15)
add_any(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
abs_add_any(-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, abs=True)
