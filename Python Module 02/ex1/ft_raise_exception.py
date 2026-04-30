def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)

    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")

    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    temp_str = ["25", "abc", "100", "-50"]

    for element in temp_str:
        print(f"Input data is '{element}'")
        try:
            temp = input_temperature(element)
            print(f"Temperature is now {temp}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
