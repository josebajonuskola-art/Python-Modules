#!/usr/bin/env python3
def display_stats(plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant._stats.grow_calls} grow, ", end='')
    print(f"{plant._stats.age_calls} age, {plant._stats.show_calls} show")
    if hasattr(plant._stats, "shade_calls"):
        print(f" {plant._stats.shade_calls} shade")


class Plant():
    class Stats:
        def __init__(self):
            self.show_calls = 0
            self.age_calls = 0
            self.grow_calls = 0

    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant.Stats()

    def show(self) -> str:
        self._stats.show_calls += 1
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def age_(self) -> None:
        self.age += 20
        self._stats.age_calls += 1

    def grow(self) -> None:
        self.height += 8
        self._stats.grow_calls += 1

    @staticmethod
    def age_checker(x: int) -> bool:
        return x > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):

    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = 0
        self._stats = Plant.Stats()

    def show(self) -> str:
        res = super().show()
        res += f"\n Color: {self.color}"
        if self.bloomed == 0:
            res += f"\n {self.name} has not bloomed yet"
        else:
            res += f"\n {self.name} is blooming beautifully!"
        return res

    def bloom(self) -> None:
        self.bloomed = 1


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = self.Stats()

    def show(self) -> str:
        res = super().show()
        res += f"\n Trunk diameter: {self.trunk_diameter}cm"
        return res

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end='')
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self._stats.shade_calls += 1

    def grow(self) -> None:
        self.height += 42
        self._stats.grow_calls += 1


class Seed(Flower):

    def __init__(self, name, height, age, color, seeds) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds
        self.bloomed = 0
        self._stats = Plant.Stats()

    def show(self) -> str:
        res = super().show()
        res += f"\n Seeds: {self.seeds}"
        return res

    def bloom(self) -> None:
        self.bloomed += 1

    def grow(self) -> None:
        self.height += 30
        self.seeds += 42
        self._stats.grow_calls += 1


def ft_garden_analytics() -> None:
    print('=== Garden statistics ===')
    print('=== Check year-old')
    print(f"Is 30 days more than a year? -> {Plant.age_checker(30)}")
    print(f"Is 400 days more than a year? -> {Plant.age_checker(400)}")
    print("\n=== Flower")
    p1 = Flower('Rose', 15.0, 10, 'red')
    print(p1.show())
    display_stats(p1)
    print("[asking the rose to grow and bloom]")
    p1.grow()
    p1.bloom()
    print(p1.show())
    display_stats(p1)
    print("\n=== Tree")
    p2 = Tree("Oak", 200.0, 365, 5.0)
    print(p2.show())
    display_stats(p2)
    print("[asking the oak to produce shade]")
    p2.produce_shade()
    display_stats(p2)
    print("\n=== Seed")
    p3 = Seed("Sunflower", 80.0, 45, "yellow", 0)
    print(p3.show())
    print("[make sunflower grow, age and bloom]")
    p3.grow()
    p3.age_()
    p3.bloom()
    print(p3.show())
    display_stats(p3)
    print("\n=== Anonymous")
    p4 = Plant.anonymous()
    print(p4.show())
    display_stats(p4)


if __name__ == "__main__":
    ft_garden_analytics()
