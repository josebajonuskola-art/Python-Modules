class GardenError(Exception):
    def __init__(self, message=None) -> None:
        if message is None:
            self.message = "Unknown garden error"
        else:
            self.message = message

    def __str__(self) -> str:
        return self.message


class PlantError(GardenError):
    def __init__(self, message=None) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message=None) -> None:
        super().__init__(message)


def low_level_det() -> None:
    raise WaterError("Not enough water in the tank!")


def wilting_detector(plant) -> None:
    raise PlantError(f"The {plant} plant is wilting!")


def ft_custom_errors() -> None:
    try:
        print("Testing PlantError...")
        wilting_detector("tomato")
        """ raise PlantError """
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("")

    try:
        print("Testing WaterError...")
        low_level_det()
        """ raise WaterError """
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        print("")

    try:
        print("Testing catching all garden errors...")
        wilting_detector("tomato")
        """ raise GardenError """
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        low_level_det()
        """ raise GardenError """
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    ft_custom_errors()
