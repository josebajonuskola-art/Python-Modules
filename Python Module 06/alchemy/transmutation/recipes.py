import alchemy.elements
from ..potions import strength_potion
import elements


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: brew "
            f"’{alchemy.elements.create_air()}’ and "
            f"’{strength_potion()}’ mixed with ’{elements.create_fire()}’")
