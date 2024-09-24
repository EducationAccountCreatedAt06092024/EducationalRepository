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
        self._flavor = value

    @property
    def is_delicious(self) -> bool:
        return not isinstance(self.flavor, str) or self.flavor.lower() != "black licorice"
