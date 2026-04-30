import os
import sys
import site


def construct() -> None:
    if "VIRTUAL_ENV" in os.environ:
        venv_path = os.environ["VIRTUAL_ENV"]
        venv_name = os.path.basename(venv_path)
        site_packs = site.getsitepackages()

        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Enviroment: {venv_name}")
        print(f"Enviroment Path: {venv_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        print(site_packs[0])

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Enviroment: None detected\n")

        print("WARNING: You're in the global enviroment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\activate # On Windows\n")

        print("Then run this program again.")


if __name__ == "__main__":
    construct()
