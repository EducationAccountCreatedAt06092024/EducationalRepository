from typing import Any, Literal, TypeAlias


class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


Strategy: TypeAlias = Literal["R", "P", "S"]
STRATEGIES: frozenset[Strategy] = frozenset({"R", "P", "S"})
RULES: dict[Strategy, Strategy] = {"R": "S", "P": "R", "S": "P"}


def rps_game_winner(moves: list[list[str]]) -> str:
    if len(moves) != 2:
        raise WrongNumberOfPlayersError

    name_1, move_1 = moves[0]
    name_2, move_2 = moves[1]

    if move_1 not in STRATEGIES or move_2 not in STRATEGIES:
        raise NoSuchStrategyError

    if RULES[move_2] == move_1:
        return f"{name_2} {move_2}"

    return f"{name_1} {move_1}"


def rps_game_winner_test():
    try:
        rps_game_winner([["A", "R"], ["B", "P"], ["C", "S"]])
    except WrongNumberOfPlayersError as e:
        print(f"{e.__class__.__name__} raised!")
    try:
        rps_game_winner([["A", "X"], ["B", "P"]])
    except NoSuchStrategyError as e:
        print(f"{e.__class__.__name__} raised!")
    assert rps_game_winner([["A", "P"], ["B", "S"]]) == "B S"
    assert rps_game_winner([["A", "P"], ["B", "P"]]) == "A P"
    print("Tests for excersize 6 completed successful")


if __name__ == "__main__":
    rps_game_winner_test()
