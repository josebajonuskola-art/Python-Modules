from abc import ABC, abstractmethod


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
        if self.status == "transformed":
            self.status = "basic"
            return (f"{self.name} stabilizes its form.")
        else:
            return (f"{self.name} is already basic")


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
