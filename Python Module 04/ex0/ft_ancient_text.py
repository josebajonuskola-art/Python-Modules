import sys
from io import open


def ancient_text() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            print("---\n")
            print(file.read(), end='')
            print("---")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        finally:
            try:
                file.close()
                print(f"\nFile '{sys.argv[1]}' closed.")
            except NameError:
                pass


if __name__ == "__main__":
    ancient_text()
