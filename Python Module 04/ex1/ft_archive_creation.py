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
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        finally:
            try:
                file.close()
                print(f"\n---\nFile '{sys.argv[1]}' closed.\n")
            except NameError:
                pass


def archive_editor() -> None:
    print("Transform data:\n---\n")
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
    if modified_file[len(modified_file) - 1] != "#":
        modified_file += ["#"]
    final_str = ""
    for element in modified_file:
        final_str += element
    print(f"{final_str}\n---\n")
    file.close()
    new_archive_creator(final_str)


def new_archive_creator(final_str: str) -> None:
    file_name = input("Enter new file name (or empty): ")
    if file_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{file_name}'")
        opened = open(f"{file_name}", "w")
        opened.write(final_str)
        print(f"Data saved in file '{file_name}'.")
        opened.close()


if __name__ == "__main__":
    archive_creation()
    archive_editor()
