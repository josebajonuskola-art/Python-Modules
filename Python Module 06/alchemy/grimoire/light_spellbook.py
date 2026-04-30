
def light_spell_allowed_ingredients() -> list:
    light_magic: list[str] = ["earth", "air", "fire", "water"]
    return (light_magic)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.light_validator import validate_ingredients
    mini_val = validate_ingredients(ingredients)
    if "INVALID" in mini_val:
        return (f"Testing record light spell: Spell rejected: {spell_name}"
                f" ({mini_val})")
    return (f"Testing record light spell: Spell recorded: {spell_name}"
            f" ({mini_val})")
