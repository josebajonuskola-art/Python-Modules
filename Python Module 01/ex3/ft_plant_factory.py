#!/usr/bin/env python3
class Plant:
    def __init__(self, name, starting_height, starting_age) -> None:
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def show(self) -> None:
        print(f"{self.name}: {self.starting_height}cm, "
              f"{self.starting_age} days old")


def ft_plant_factory() -> None:
    plant: list[Plant] = [Plant(*data) for data in [
        ('Rose', 25.0, 30),
        ('Oak', 200.0, 365),
        ('Cactus', 5.0, 90),
        ('Sunflower', 80.0, 45),
        ('Fern', 15.0, 120)]]
    print('=== Plant Factory Output ===')
    for i in range(len(plant)):
        print('Created: ', end='')
        plant[i].show()


if __name__ == "__main__":
    ft_plant_factory()
