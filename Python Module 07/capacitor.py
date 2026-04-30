from ex1.class_file import HealingCreatureFactory, TransformCreatureFactory


def healing_creatures() -> None:

    # Heal capability
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()
    base_heal = heal_factory.create_base()
    evolve_heal = heal_factory.create_evolved()

    # Base heal
    print(" base:")
    print(f"{base_heal.describe()}")
    print(f"{base_heal.attack()}")
    print(f"{base_heal.heal()}")

    # Evolve heal
    print(" evolved:")
    print(f"{evolve_heal.describe()}")
    print(f"{evolve_heal.attack()}")
    print(f"{evolve_heal.heal()}")


def transforming_creatures() -> None:

    # Transform capability
    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    base_transform = transform_factory.create_base()
    evolve_transform = transform_factory.create_evolved()

    # Base transform
    print(" base:")
    print(f"{base_transform.describe()}")
    print(f"{base_transform.attack()}")
    print(f"{base_transform.transform()}")
    print(f"{base_transform.attack()}")
    print(f"{base_transform.revert()}")

    # Evolve transform
    print(" evolved:")
    print(f"{evolve_transform.describe()}")
    print(f"{evolve_transform.attack()}")
    print(f"{evolve_transform.transform()}")
    print(f"{evolve_transform.attack()}")
    print(f"{evolve_transform.revert()}")


def main() -> None:
    healing_creatures()
    transforming_creatures()


if __name__ == "__main__":
    main()
