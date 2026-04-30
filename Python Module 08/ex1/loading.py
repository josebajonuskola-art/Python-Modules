def still_loading() -> None:

    is_possible = True
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    try:
        import pandas as pd    # type: ignore
        print(f"[OK] pandas {pd.__version__} - Data manipulation ready")
    except ImportError:
        print("[KO] pandas - Data manipulation not ready")
        is_possible = False

    try:
        import numpy as np    # type: ignore
        print(f"[OK] numpy {np.__version__} - Numerical computation ready")
    except ImportError:
        print("[KO] numpy - Numerical computation not ready")
        is_possible = False

    try:
        import requests    # type: ignore
        print(f"[OK] requests {requests.__version__} - Network access ready")
    except ImportError:
        print("[KO] requests - Network access not ready")
        is_possible = False

    try:
        import matplotlib    # type: ignore
        import matplotlib.pyplot as plt    # type: ignore
        print(f"[OK] matplotlib {matplotlib.__version__} - "
              "Visualization ready")
    except ImportError:
        print("[KO] matplotlib - Visualization not ready")
        is_possible = False

    if is_possible:
        # Generating 1000 random numbers, the average of the numbers is 0
        # The standard deviation is 24
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        data_points = np.random.normal(0, 24, 1000)

        # Proccess the data with panda
        df = pd.DataFrame({'data': data_points})
        print(f"Mean value: {df['data'].mean():.2f}")

        # Generate the graphic
        print("Generating visualization...\n")
        plt.figure(figsize=(10, 6))
        plt.hist(data_points, bins=60, edgecolor='blue')
        plt.title('Matrix Data Analysis')
        plt.xlabel('Values')
        plt.ylabel('Frequency')

        # Save the info in the .png
        plt.savefig('matrix_analysis.png')
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    else:
        print("Impossible to continue with the function, "
              "neccesary libraries aren't installed")

    # Differences between pip and poetry
    print("pip vs Poetry\n")

    print("pip:")
    print("- Installs Python packages")
    print("- Uses requirements.txt")
    print("- Needs venv for environments")
    print("- Simple and flexible")
    print("- Manual dependency management\n")

    print("Poetry:")
    print("- Manages packages and environments")
    print("- Uses pyproject.toml")
    print("- Creates environments automatically")
    print("- More structured and reproducible")
    print("- Better dependency resolution\n")

    print("Summary:")
    print("pip = simple package installer")
    print("Poetry = complete project manager")


if __name__ == "__main__":
    still_loading()


# To run poetry first we have to install it -> "pip install poetry" or
# "curl -sSL https://install.python-poetry.org | python3 -"

# Method 1: Using poetry new (Recommended for new projects)
# 1. Create project structure: poetry new <project_name>
# 2. Navigate to project: cd <project_name>
# 3. Add modules: poetry add <module_1> <module_2> ...
# 4. Install dependencies: poetry install --no-root
# 5. Run program: poetry run python <name_of_file>

# Method 2: Using poetry init (For existing projects)
# 1. Create pyproject.toml in current directory: poetry init
# 2. Skip unnecessary information when prompted
# 3. When "Package to add or search for" appears, add modules one by one
# 4. Answer yes/no to development dependencies as needed, normally write "no"
# 5. Confirm the generation "Do you confirm generation? (yes/no) [yes] yes"
# 5. Install dependencies: poetry install --no-root
# 6. Run program: poetry run python <name_of_file>
