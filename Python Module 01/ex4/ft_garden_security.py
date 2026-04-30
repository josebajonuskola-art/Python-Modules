#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name, _height, _age) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        if _height < 0:
            print(f"\n{self.name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = _height
        if _age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print('Age update rejected\n')
        else:
            self._age = _age

    def get_height(self) -> float:
        return float(self._height)

    def get_age(self) -> int:
        return self._age

    def set_height(self, x) -> None:
        if x < 0:
            print(f"\n{self.name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = x
            print(f"Height updated: {x}cm")

    def set_age(self, x) -> None:
        if x < 0:
            print(f"{self.name}: Error, age can't be negative")
            print('Age update rejected\n')
        else:
            self._age = x
            print(f"Age updated: {x} days")

    def print_name(self) -> None:
        print(f"Plant created: {self.name}: {self._height}cm,", end='')
        print(f" {self._age} days old")

    def updated_plant(self) -> None:
        print(f"Current state: {self.name}:", end='')
        print(f" {self.get_height()}cm, {self.get_age()} days old")


def ft_garden_security() -> None:
    print('=== Garden Security System ===')
    p1 = SecurePlant('Rose', 15, 10)
    p1.print_name()
    print("")
    p1.set_height(25)
    p1.set_age(30)
    p1.set_height(-5)
    p1.set_age(-13)
    p1.updated_plant()


if __name__ == "__main__":
    ft_garden_security()
