from typing import Any


def connect_dicts(a: dict[Any, int], b: dict[Any, int]) -> dict[Any, int]:
    a_value, b_value = sum(a.values()), sum(b.values())

    if a_value > b_value:
        main, secondary = a, b
    else:
        main, secondary = b, a

    connected: list[tuple[Any, int]] = []

    keys = set()
    keys.update(main.keys())
    keys.update(secondary.keys())
    for key in keys:
        value = main.get(key, secondary.get(key))
        connected.append((key, value))  # type: ignore

    return dict(sorted(filter(lambda x: x[1] > 10, connected), key=lambda x: x[1]))


def connect_dicts_test():
    print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
    assert connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}) == {"c": 11, "b": 12}
    print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
    assert connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}) == {"d": 11, "c": 12, "a": 13}
    print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
    assert connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}) == {"c": 11, "b": 12, "a": 15}
    print("Tests for excersize 9 completed successful, but keys order must be checked manually")


if __name__ == "__main__":
    connect_dicts_test()
