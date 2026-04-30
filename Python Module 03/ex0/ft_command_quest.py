import sys


def ft_command_quest() -> None:
    i = 0
    print("=== Command Quest ===")
    print("Program name:", sys.argv[i])
    length = len(sys.argv) - 1
    i = 1
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length}")
        while i < len(sys.argv):
            print(f"Argument {i}:", sys.argv[i])
            i += 1
    print("Total arguments:", len(sys.argv))
    print("")


if __name__ == "__main__":
    ft_command_quest()
