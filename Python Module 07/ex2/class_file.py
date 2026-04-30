from abc import ABC, abstractmethod
from typing import cast


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.status = "basic"

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class Creature(ABC):

    def __init__(self, name: str, type1: str) -> None:
        self.name = name
        self.type1 = type1

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.type1} type Creature")


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)
        self.status = "basic"

    def attack(self) -> str:
        if self.status == "basic":
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} performs a boosted strike!")

    def transform(self) -> str:
        if self.status == "basic":
            self.status = "transformed"
            return (f"{self.name} shifts into a sharper form!")
        else:
            return (f"{self.name} is already transformed")

    def revert(self) -> str:
        if self.status == "transformed":
            self.status = "basic"
            return (f"{self.name} returns to normal.")
        else:
            return (f"{self.name} is already basic")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)
        self.status = "basic"

    def attack(self) -> str:
        if self.status == "basic":
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} unleashes a devastating morph strike!")

    def transform(self) -> str:
        if self.status == "basic":
            self.status = "transformed"
            return (f"{self.name} morphs into a dragonic battle form!")
        else:
            return (f"{self.name} is already transformed")

    def revert(self) -> str:
        if self.status == "basic":
            return (f"{self.name} is already basic")
        else:
            self.status = "basic"
            return (f"{self.name} stabilizes its form.")


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception("Invalid Creature "
                            f"'{creature.name}' for this aggressive strategy")
        transform_creature = cast(TransformCapability, creature)
        print(transform_creature.transform())
        print(creature.attack())
        print(transform_creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError("Invalid Creature "
                             f"'{creature.name}' for this defensive strategy")
        transform_creature = cast(HealCapability, creature)
        print(creature.attack())
        print(transform_creature.heal())


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
