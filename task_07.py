from collections import Counter


def combine_anagrams(words: list[str]) -> list[list[str]]:
    groups: list[tuple[Counter, list]] = []

    for word in words:
        current_key = Counter(word)
        for key, anagrams in groups:
            if key == current_key:
                anagrams.append(word)
                break
        else:
            groups.append((current_key, [word]))

    return [anagrams for _, anagrams in groups]


def combine_anagrams_test():
    print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
    print("Tests for excersize 7 must be checked manually")


if __name__ == "__main__":
    combine_anagrams_test()
