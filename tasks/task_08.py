from typing import Any
from functools import reduce
from operator import mul


def multiply_numbers(obj: Any = None) -> int | None:
    try:
        return reduce(mul, map(int, filter(str.isdigit, str(obj))))
    except TypeError:  # empty sequence
        return None


def multiply_numbers_test():
    assert multiply_numbers() is None
    assert multiply_numbers("ss") is None
    assert multiply_numbers("1234") == 24
    assert multiply_numbers("sssdd34") == 12
    assert multiply_numbers(2.3) == 6
    assert multiply_numbers([5, 6, 4]) == 120
    print("Tests for excersize 8 completed successful")


if __name__ == "__main__":
    multiply_numbers_test()
