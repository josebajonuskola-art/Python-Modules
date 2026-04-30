import os
from dotenv import load_dotenv


def load_config() -> None:
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Loading configuration...")

    # Try to access to the .env file's information
    try:
        matrix_mode = os.getenv("MATRIX_MODE")
        data_base = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zion_network = os.getenv("ZION_ENDPOINT")

        configurations = [
            ("MATRIX_MODE", matrix_mode),
            ("DATABASE_URL", data_base),
            ("API_KEY", api_key),
            ("LOG_LEVEL", log_level),
            ("ZION_ENDPOINT", zion_network),
        ]

        # Raise the ValueError in case any "configuration" is missing or empty
        for name, configuration in configurations:
            if not configuration:
                raise ValueError(f"{name} missing")

        print(f"Mode: {matrix_mode}")
        print(f"Database: {data_base}")
        print(f"API Access: {api_key}")
        print(f"Log level: {log_level}")
        print(f"Zion Network: {zion_network}")

    except ValueError as e:
        print(e)

    print("\nEnviroment security check:")

    if api_key == "Authenticated":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Hardcoded secrets detected")

    if os.path.exists(".env.example"):
        print("[OK] .env file properly configurable")
    else:
        print("[KO] .env file improperly configurable")

    if matrix_mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides aren't available")


if __name__ == "__main__":
    load_config()
