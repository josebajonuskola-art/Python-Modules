def secure_archive(
    file_name: str,
    action: int,
    content: str | None = None
) -> tuple[bool, str]:
    if action == 0:
        try:
            with open(f"{file_name}", "r") as file:
                read = file.read()
                tuplelini = (True, f"{read}")
        except Exception as e:
            tuplelini = (False, f"{e}")
        finally:
            return tuplelini
    else:
        try:
            with open(f"{file_name}", "w") as file:
                file.write(f"{content}")
                tuplelini = (
                    True,
                    "Content successfully written to file"
                            )
        except Exception as e:
            tuplelini = (False, f"{e}")
        finally:
            return tuplelini


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('/not/existing/file', 0)}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('master.passwd', 0)}\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('ancient_fragment.txt', 0)}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive('new_file', 1, "Content successfully"
                            f"written to file")}")


if __name__ == "__main__":
    main()
