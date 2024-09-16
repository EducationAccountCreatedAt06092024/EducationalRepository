from typing import Any


def max_odd(array: list[Any]) -> float | None:
    eps = 10**-6
    return max(
        filter(lambda x: isinstance(x, (int, float)) and abs(x % 2 - 1) < eps, array),
        default=None,
    )


def max_odd_test():
    assert max_odd([1, 2, 3, 4, 4]) == 3
    assert max_odd([21.0, 2, 3, 4, 4]) == 21
    assert max_odd(["ololo", 2, 3, 4, [1, 2], None]) == 3
    assert max_odd(["ololo", "fufufu"]) is None
    assert max_odd([2, 2, 4]) is None
    print("Tests for excersize 3 completed successful")


if __name__ == "__main__":
    max_odd_test()
