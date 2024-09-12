from typing import Any


def coincidence(lst: list[Any] | None = None, rng: range | None = None) -> list[float]:
    if lst is None or rng is None:
        return []

    return [e for e in lst if isinstance(e, (int, float)) and rng.start <= e < rng.stop]


def coincidence_test():
    assert coincidence([1, 2, 3, 4, 5], range(3, 6)) == [3, 4, 5]
    assert coincidence() == []
    assert coincidence([None, 1, "foo", 4, 2, 2.5], range(1, 4)) == [1, 2, 2.5]
    print("Tests for excersize 2 completed successful")


if __name__ == "__main__":
    coincidence_test()
