from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, type1: str) -> None:
        self.name = name
        self.type1 = type1

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.type1} type Creature")


class Flameling(Creature):

    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Pyrodon(Creature):

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):

    def attack(self) -> str:
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):

    def attack(self) -> str:
        return ("Torragon uses Hydro Pump!")


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return (Flameling("Flameling", "Fire"))

    def create_evolved(self) -> Creature:
        return (Pyrodon("Pyrodon", "Fire/Flying"))


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Aquabub("Aquabub", "Water"))

    def create_evolved(self) -> Creature:
        return (Torragon("Torragon", "Water"))
