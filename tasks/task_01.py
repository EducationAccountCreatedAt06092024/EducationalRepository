from typing import Any


def is_palindrome(obj: Any) -> bool:
    string = str(obj)
    pure_string = "".join(e for e in str(string) if e.isalnum()).lower()
    length = len(pure_string)

    for i in range(length // 2):
        if pure_string[i] != pure_string[length - 1 - i]:
            return False

    return True


def is_palindrome_test():
    assert is_palindrome("A man, a plan, a canal -- Panama")
    assert is_palindrome("Madam, I'm Adam!")
    assert is_palindrome(333)
    assert not is_palindrome(None)
    assert not is_palindrome("Abracadabra")
    print("Tests for excersize 1 completed successful")


if __name__ == "__main__":
    is_palindrome_test()
