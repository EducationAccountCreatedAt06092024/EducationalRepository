from typing import Any


class Dessert:
    
    def __init__(self, name: str | None = None, calories: float | None = None):
        self._name = name
        self._calories = calories

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: Any) -> None:
        self._name = value

    @property
    def calories(self) -> float | None:
        return self.calories

    @calories.setter
    def calories(self, value: Any) -> None:
        self._calories = value

    @property
    def is_healthy(self) -> bool:
        return isinstance(self._calories, (int, float)) and self._calories < 200

    @property
    def is_delicious(self) -> bool:
        return True
