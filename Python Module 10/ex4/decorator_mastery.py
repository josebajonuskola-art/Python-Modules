import time
from functools import wraps
from collections.abc import Callable
from typing import Any


def power_validator(min_power: int) -> Callable:

    def validate_power(cast_spell: Callable) -> Callable:

        @wraps(cast_spell)
        def enough(*arg: Any, **kwargs: Any) -> Callable | str:
            if arg[2] >= min_power:
                return cast_spell(*arg, **kwargs)
            else:
                return "Insufficient power for this spell"

        return enough

    return validate_power


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def timer(*args: Any, **kwargs: Any) -> Any:

        t1 = time.time()
        print(f"Casting {func.__name__}...")
        res = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - t1:.3f} seconds")
        # It doesn't take long enough to be appreciated with 3 decimals
        return res

    return timer


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        has_space = False
        has_alpha = False

        if len(name) < 3:
            return False

        for ch in name:

            if ch.isalpha():
                has_alpha = True

            elif ch.isspace():
                has_space = True

            else:
                return False

        if has_alpha and has_space:
            return True

        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def retry_spell(max_attempts: int) -> Callable:

    def receive_the_func(func: Callable) -> Callable:

        @wraps(func)
        def retrying_the_spell(*args: Any, **kwargs: Any) -> str | int:

            i = 0
            while i < max_attempts:

                try:
                    str_spell = func(*args, **kwargs)
                    res = int(str_spell)
                    return int(res)

                except Exception:
                    print(
                        f"Spell failed, retrying... (attempt {i + 1}/"
                        f"{max_attempts})")

                i += 1

            return (f"Spell casting failed after {i} "
                    "attempts\nWaaaaaaagh spelled !")

        return retrying_the_spell

    return receive_the_func


@spell_timer
def fireball() -> str:
    return "Result: Fireball cast!"


@retry_spell(3)
def failed_spell() -> str:
    return "String spell"


def main() -> None:

    mage = MageGuild()

    # Spell timer
    print("\nTesting spell timer...")
    print(fireball())

    # Retry spell
    print("\nTesting retrying spell...")
    print(failed_spell())

    # MageGuild class
    print("\nTesting MageGuild...")
    print("Testing Mage names...")
    print("Testing 'The Great juskola' mage name: "
          f"{MageGuild.validate_mage_name('The Great juskola')}")
    print("Testing '    ' mage name: "
          f"{MageGuild.validate_mage_name('   ')}")
    print("Testing 'juskola' mage name: "
          f"{MageGuild.validate_mage_name('juskola')}")
    print("Testing '  angryEvaluator333' mage name: "
          f"{MageGuild.validate_mage_name('  angryEvaluator333')}")
    print("Testing spell casting min power...")
    print(mage.cast_spell("Lightning", 25))
    print(mage.cast_spell("Fireless fireball", 9))


if __name__ == "__main__":
    main()
