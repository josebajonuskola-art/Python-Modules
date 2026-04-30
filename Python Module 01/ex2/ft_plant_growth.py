#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self) -> None:
        a = round(self.height, 1)
        print(f"{self.name}: {a}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1


def ft_plant_growth() -> None:
    p1 = Plant('Rose', 25.0, 30)
    p1.show()
    initial_height = p1.height
    print('=== Day 1 ===')
    p1.age()
    p1.grow()
    p1.show()

    days = int(7 - 1)
    for i in range(days):
        print(f"=== Day {i + 2} ===")
        p1.grow()
        p1.age()
        p1.show()
    growth = round(p1.height - initial_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()
