from task_11 import Dessert


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
