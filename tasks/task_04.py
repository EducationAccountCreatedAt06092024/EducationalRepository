from typing import Any


def sort_list(lst: list[int]) -> None:
    min_elem, max_elem = None, None
    for e in lst:
        if min_elem is None or e < min_elem:
            min_elem = e
        if max_elem is None or e > max_elem:
            max_elem = e

    if min_elem is None or max_elem is None:
        return

    if min_elem != max_elem:
        for i, e in enumerate(lst):
            if e == min_elem:
                lst[i] = max_elem
            elif e == max_elem:
                lst[i] = min_elem

    lst.append(min_elem)
    return


def sort_list_test():
    lst = []
    sort_list(lst)
    assert lst == []
    lst = [2, 4, 6, 8]
    sort_list(lst)
    assert lst == [8, 4, 6, 2, 2]
    lst = [1]
    sort_list(lst)
    assert lst == [1, 1]
    lst = [1, 2, 1, 3]
    sort_list(lst)
    assert lst == [3, 2, 3, 1, 1]
    print("Tests for excersize 4 completed successful")


if __name__ == "__main__":
    sort_list_test()
