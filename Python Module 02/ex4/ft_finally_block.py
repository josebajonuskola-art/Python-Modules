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


def water_plant(plant_name) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plants in valid_plants:
            water_plant(plants)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    invalid_plants = ["Tomato", "lettuce"]
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        for plants in invalid_plants:
            water_plant(plants)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
