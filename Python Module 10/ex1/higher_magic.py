from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return (f"Heal restores {target} for {power} HP")


def fireball(target: str, power: int) -> str:
    return (f"Fireball hits {target} with {power} damage points")


def back_stab(target: str, power: int) -> str:
    return (f"{target} back stabs with {power} damage points")


def power_condition(target: str, power: int) -> bool:
    return power >= 5


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combiner(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplifier(target: str, power: int) -> Callable:
        return (base_spell(target, power * multiplier))

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def caster(target: str, power: int) -> Callable | str:

        if condition(target, power):
            return spell(target, power)
        else:
            return ("Spell fizzled")

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequencer(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequencer


def main() -> None:

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    res_combined = combined("Dragon", 24)
    print("Combined spell result: ", end='')
    print(*res_combined)

    print("\nTesting power amplifier...")
    goblin = ("Goblin", 3)
    amplified = power_amplifier(back_stab,  10)
    res_amplified = amplified("Goblin", 3)
    print(f"Original {goblin[0]}'s power: "
          f"{back_stab('Goblin', 3)}, Amplified "
          f"{goblin[0]}'s power: {res_amplified}")

    print("\nTesting conditional caster...")
    print("Testing with a true condition...")
    true_casted = conditional_caster(power_condition, fireball)
    true_res_casted = true_casted("Dragon", 24)
    print(true_res_casted)
    print("Testing with false condition...")
    false_casted = conditional_caster(power_condition, back_stab)
    false_res_casted = false_casted("Goblin", 3)
    print(false_res_casted)

    print("\nTesting spell sequence...")
    sequence_of_spells = [back_stab, fireball, heal]
    spell_sequenced = spell_sequence(sequence_of_spells)
    res_sequenced = spell_sequenced("Dragon", 25)
    print(', '.join(res_sequenced))


if __name__ == "__main__":

    main()
