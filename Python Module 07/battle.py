from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:

    base = factory.create_base()
    evolve = factory.create_evolved()

    print("Testing factory")

    print(f"{base.describe()}")
    print(f"{base.attack()}")

    print(f"{evolve.describe()}")
    print(f"{evolve.attack()}")
    print()


def test_battle(factory1: FlameFactory, factory2: AquaFactory) -> None:
    flame_base = factory1.create_base()
    aqua_base = factory2.create_base()

    print("Testing battle")
    print(f"{flame_base.describe()}")
    print(" vs.")
    print(f"{aqua_base.describe()}")

    print("fight!")
    print(f"{flame_base.attack()}")
    print(f"{aqua_base.attack()}")


def main() -> None:
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
