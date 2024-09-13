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


class JellyBean(Dessert):
    
    def __init__(self, name: str | None = None, calories: float | None = None, flavor: str | None = None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self) -> str | None:
        return self._flavor

    @flavor.setter
    def flavor(self, value) -> None:
        if isinstance(value, str) or value is None:
            self._flavor = value
        else:
            raise ValueError("flavor must be str | None")

    @property
    def is_delicious(self) -> bool:
        return self.flavor is None or self.flavor.lower() != "black licorice"
