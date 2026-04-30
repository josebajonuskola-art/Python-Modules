from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    dark_magic: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return (dark_magic)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    mini_val = validate_ingredients(ingredients)
    if "INVALID" in mini_val:
        return (f"Testing record dark spell: Spell rejected: {spell_name} "
                f"({mini_val})")
    return (f"Testing record dark spell: Spell recorded: {spell_name} "
            f"({mini_val})")
