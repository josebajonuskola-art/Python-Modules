from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    list = light_spell_allowed_ingredients()
    to_lower = ingredients.lower()
    is_valid = any(word in to_lower for word in list)
    status = "VALID" if is_valid else "INVALID"
    return (f"{ingredients} - {status}")
