#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 42

    def age_(self) -> None:
        self.age += 20

    def show(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = 0

    def show(self) -> str:
        res = super().show()

        res += f"\n Color: {self.color}"
        if self.bloomed == 0:
            res += (f"\n {self.name} has not bloomed yet")
        else:
            res += (f"\n {self.name} is blooming beautifully!\n")
        return res

    def bloom(self) -> None:
        self.bloomed = 1


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> str:
        res = super().show()
        res += f"\n Trunk diameter: {self.trunk_diameter}cm"
        return res

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end='')
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> str:
        res = super().show()
        res += f"\n Harvest season: {self.harvest_season}"
        res += f"\n Nutritional value: {self.nutritional_value}"
        return res

    def age_(self) -> None:
        super().age_()

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 20


def ft_plant_types() -> None:
    print('=== Garden Plant Types ===')
    p1 = Flower('Rose', 15.0, 10, 'red')
    p2 = Tree('Oak', 200.0, 365, 5.0)
    p3 = Vegetable('Tomato', 5.0, 10, 'April', 0)
    print("=== Flower")
    print(p1.show())
    print("[asking the rose to bloom]")
    p1.bloom()
    print(p1.show())
    print("=== Tree")
    print(p2.show())
    print("[asking the oak to produce shade]")
    p2.produce_shade()
    print("=== Vegetable")
    print(p3.show())
    print("[make tomato grow and age for 20 days]")
    p3.age_()
    p3.grow()
    print(p3.show())


if __name__ == "__main__":
    ft_plant_types()
