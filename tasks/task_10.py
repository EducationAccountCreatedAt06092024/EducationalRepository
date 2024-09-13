from collections import Counter


def count_words(text: str) -> dict[str, int]:
    words = []
    buffer = []
    for char in text.lower():
        if char.isalpha():
            buffer.append(char)
        elif buffer:
            words.append("".join(buffer))
            buffer = []

    if buffer:
        words.append("".join(buffer))

    return dict(Counter(words))


def count_words_test():
    assert count_words("A man, a plan, a canal -- Panama") == {"a": 3, "man": 1, "plan": 1, "canal": 1, "panama": 1}
    assert count_words("Doo bee doo bee doo") == {"doo": 3, "bee": 2}
    print("Tests for excersize 10 completed successful")


if __name__ == "__main__":
    count_words_test()
