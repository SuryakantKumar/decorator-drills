"""Import 'functools' module of python"""
import functools


@functools.lru_cache(maxsize=None)
def factorial(n):
    """Factorial of a given number"""

    print("Computing factorial({})".format(n))
    if n == 1:
        return 1
    return n * factorial(n-1)


factorial(497)
# factorial(100)

print(factorial.cache_info())
