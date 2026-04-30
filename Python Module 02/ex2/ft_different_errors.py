def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        number = int("abc")
        number += 1
    elif operation_number == 1:
        zerodiv = 1300 / 0
        zerodiv += 1
    elif operation_number == 2:
        open('/non/existent/file', 'r')
    elif operation_number == 3:
        typer = 'hello' + 5
        typer += "world"


def test_error_types() -> None:
    i = 0
    while i <= 4:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
