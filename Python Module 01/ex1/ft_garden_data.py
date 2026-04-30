#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    print('=== Garden Plant Registry ===')
    p1 = Plant('Rose', 25, 30)
    p2 = Plant('Sunflower', 80, 45)
    p3 = Plant('Cactus', 15, 120)
    p1.show()
    p2.show()
    p3.show()


if __name__ == "__main__":
    ft_garden_data()
