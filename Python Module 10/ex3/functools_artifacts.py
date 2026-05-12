from typing import Any
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator


def base_enchantment(power: int, element: str, target: str) -> str:
    return (f"{target} is now a {element} {target} with {power} power points")


def spell_reducer(spells: list[int], operation: str) -> int:

    if len(spells) == 0:
        return 0

    if operation == "add":
        return (reduce(operator.add, spells))

    elif operation == "multiply":
        return (reduce(operator.mul, spells))

    elif operation == "max":
        return (reduce(lambda x, y: x if x > y else y, spells))

    elif operation == "min":
        return (reduce(lambda x, y: x if x < y else y, spells))

    else:
        raise ValueError("Introduce a valid operation please... "
                         "The opartion must be one of these 'add', "
                         "'multiply', 'max' or 'min'")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    return {
        "flame_sword": partial(base_enchantment, power=50, element="flaming"),
        "frozen_sword": partial(base_enchantment, power=50, element="frozen"),
        "cursed_sword": partial(base_enchantment, power=50, element="cursed"),
    }


def memoized_fibonacci(n: int) -> int:

    @lru_cache
    def fibonacci(n: int) -> int:
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci(n)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(arg: Any) -> str:
        return ("Unknown spell type")

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return (f"Damage spell: {arg} damage")

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return (f"Enchantment: {arg}")

    @dispatcher.register(list)
    def _(arg: list[Any]) -> str:

        i = 0
        for element in arg:
            i += 1
        return (f"Multi-cast: {i} spells")

    return dispatcher


def main() -> None:

    # Spell reducer
    print("\nTesting spell reducer...")
    spells_power = [100, 400, 36]
    empty_spells_list: Any = []

    try:

        print("Sum of the spells: "
              f"{spell_reducer(spells_power, 'add')}")
        print("Product of the spells: "
              f"{spell_reducer(spells_power, 'multiply')}")
        print("Maximum power of the spells: "
              f"{spell_reducer(spells_power, 'max')}")
        print("Minimal power of the spells: "
              f"{spell_reducer(spells_power, 'min')}")
        print("Testing with an empty spells list...")
        print("Minimal power of the spells: "
              f"{spell_reducer(empty_spells_list, 'min')}")
        print("Testing invalid operation...")
        print("Average power of the spells: "
              f"{spell_reducer(spells_power, 'avergae')}")

    except ValueError as e:

        print(e)

    # Partial enchanter
    print("\nTesting partial enchanter...")
    enchanted_swords = partial_enchanter(base_enchantment)
    for sword in enchanted_swords:
        print(enchanted_swords[sword](target="Sword"))

    # Memoized fibonacci
    print("\nTesting memoized fibonacci...")
    top_fibonacci = memoized_fibonacci(18)
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(18): {top_fibonacci}")

    # Spell dispatcher
    print("\nTesting spell dispatcher...")
    list_of_spells = ["fireball", "frozen_stab", "healing_spell"]
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch('fireball'))
    print(dispatch(list_of_spells))
    print(dispatch(23.5))


if __name__ == "__main__":
    main()
