def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    try:
        temp = input_temperature(valid_input)
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    invalid_input = "abc"
    print(f"Input data is '{invalid_input}'")
    try:
        temp = input_temperature(invalid_input)
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


def ft_first_exception() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    ft_first_exception()
