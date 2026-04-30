import sys
from io import open


def archive_creation() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(f"{sys.argv[1]}", "r")
            print("---\n")
            print(file.read(), end='')
            file.close()
            print(f"\n\n---\nFile '{sys.argv[1]}' closed.\n")
            archive_editor()
        except Exception as e:
            print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n",
                  file=sys.stderr)


def archive_editor() -> None:
    print("\nTransform data:\n---\n")
    file = open(f"{sys.argv[1]}", "r")
    new_file = []
    for line in file:
        new_file += list(line)
    file.close()
    i = 0
    modified_file = []
    length = len(new_file)
    while i < length:
        if new_file[i] == '\n' and i < length:
            modified_file += ["#"]
            modified_file += ['\n']
        else:
            modified_file += new_file[i]
        i += 1
    if modified_file and modified_file[-1] != "#":
        modified_file += ["#"]
    final_str = ""
    for element in modified_file:
        final_str += element
    print(f"{final_str}\n\n---")
    file.close()
    new_archive_creator(final_str)


def new_archive_creator(final_str: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    file_name = sys.stdin.readline().strip('\n')
    # sys.stdout.write -> is used to print the first message.
    # It could be also using the print fucntion
    # sys.stdout.flush -> forces the buffer to be written immediately
    # to the output.
    # sys.stdin.readline().strip('\n') -> reads a line from
    # standard input (stdin), including the trailing newline character
    # in the stdin . Strip is used to remove the newline
    if file_name == "":
        print("Not saving data.")
    else:
        try:
            opened = open(file_name, "w")
            opened.write(final_str)
            opened.close()
            print(f"Data saved in file '{file_name}'.")
        except Exception as e:
            print(
                    f"[STDERR] Error opening file '{file_name}': {e}",
                    file=sys.stderr
                    )
            print("Data not saved.")


if __name__ == "__main__":
    archive_creation()
