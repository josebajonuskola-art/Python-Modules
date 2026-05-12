from collections.abc import Callable


def mage_counter() -> Callable:

    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    total = initial_power

    def accumulator(power_to_add: int) -> int:

        nonlocal total
        total += power_to_add
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def factory(item: str) -> str:
        return (f"{enchantment_type} {item}")

    return factory


def memory_vault() -> dict[str, Callable]:

    vault: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        vault.update({key: value})

    def recall(key: str) -> int | str:
        try:
            return vault[key]

        except KeyError:
            return ("Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:

    # Mage counter
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print(f"counter_b call 2: {counter_b()}")

    # Spell accumulator
    print("\nTesting spell accumulator...")
    initial_value = 100
    value_to_add = 20
    for i in range(2):
        accumulated = spell_accumulator(initial_value)
        res_accumulated = accumulated(value_to_add)
        print(f"Base {initial_value}, add {value_to_add}: {res_accumulated}")
        value_to_add += 10
        initial_value = res_accumulated

    # Enchantment factoy
    print("\nTesting enchantment factory...")
    flame_enchantment = enchantment_factory("Flaming")
    flaming_sword = flame_enchantment("Sword")
    print(flaming_sword)
    frozen_enchantment = enchantment_factory("Frozen")
    frozen_shield = frozen_enchantment("Shield")
    print(frozen_shield)

    # Memory vault
    print("\nTesting memory vault...")
    stored = memory_vault()
    stored['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {stored['recall']('secret')}")
    print(f"Recall 'unknown': {stored['recall']('unknown')}")


if __name__ == "__main__":
    main()
