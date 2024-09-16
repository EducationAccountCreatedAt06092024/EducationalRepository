from typing import Any
import datetime


def date_in_future(integer: Any) -> str:
    shift = datetime.timedelta(days=integer) if isinstance(integer, int) else datetime.timedelta()
    return (datetime.datetime.now() + shift).strftime("%d-%m-%Y %H:%M:%S")


def date_in_future_test():
    print(date_in_future([]))
    print(date_in_future(2))
    print("Tests for excersize 5 must be checked manually")


if __name__ == "__main__":
    date_in_future_test()
