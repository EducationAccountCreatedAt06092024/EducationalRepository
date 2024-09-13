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
        if isinstance(value, str) or value is None:
            self._name = value
        else:
            raise ValueError("name must be str | None")

    @property
    def calories(self) -> float | None:
        return self.calories

    @name.setter
    def name(self, value: Any) -> None:
        if isinstance(value, int):
            self._calories = float(value)
        elif isinstance(value, float) or value is None:
            self._calories = value
        else:
            raise ValueError("calories must be int | float | None")

    @property
    def is_healthy(self) -> bool:
        return self._calories is not None and self._calories < 200

    @property
    def is_delicious(self) -> bool:
        return True
