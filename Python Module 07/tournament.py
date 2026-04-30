from ex2.class_file import CreatureFactory, HealingCreatureFactory
from ex2.class_file import TransformCreatureFactory
from ex2.class_file import BattleStrategy, NormalStrategy, AggressiveStrategy
from ex2.class_file import DefensiveStrategy
from ex2.class_file import FlameFactory, AquaFactory


def brawlers_list_printer(brawlers: list[tuple[CreatureFactory,
                                               BattleStrategy]]) -> int:
    brawlers_list = []
    i = 0
    for brawler in brawlers:
        strategy_name = brawler[1].__class__.__name__.replace("Strategy", "")

        if isinstance(brawler[0], FlameFactory):
            brawlers_list.append(f"(Flameling+{strategy_name})")

        elif isinstance(brawler[0], AquaFactory):
            brawlers_list.append(f"(Aquabub+{strategy_name})")

        elif isinstance(brawler[0], HealingCreatureFactory):
            brawlers_list.append(f"(Healing+{strategy_name})")

        elif isinstance(brawler[0], TransformCreatureFactory):
            brawlers_list.append(f"(Transform+{strategy_name})")

        i += 1

    print(f"{brawlers_list}")
    return (i)


def battle_func(tournament: str, brawlers: list[tuple[CreatureFactory,
                                                BattleStrategy]]) -> None:

    print(f"{tournament}")
    i = 0
    i = brawlers_list_printer(brawlers)
    print(f"*** Tournament ***\n{i} opponents involved\n")
    i = 0
    j = 0
    while i <= len(brawlers) + 1:
        while j < len(brawlers):
            if j > i:
                try:
                    print("* Battle *")
                    creature1 = brawlers[i][0].create_base()
                    creature2 = brawlers[j][0].create_base()
                    print(creature1.describe())
                    print(" vs.")
                    print(creature2.describe())
                    print(" now fight!")
                    brawlers[i][1].act(creature1)
                    brawlers[j][1].act(creature2)
                    print()
                except Exception as e:
                    print(f"Battle error, aborting tournament: {e}")
                    return
            j += 1
        j = i
        i += 1


if __name__ == "__main__":

    battle_func("Tournament 0 (basic)", [(FlameFactory(),
                                          NormalStrategy()),
                                         (HealingCreatureFactory(),
                                          DefensiveStrategy())])
    print()
    battle_func("Tournament 1 (error)", [(FlameFactory(),
                                          AggressiveStrategy()),
                                         (HealingCreatureFactory(),
                                          DefensiveStrategy())])
    print()
    battle_func("Tournament 2 (multiple)", [(AquaFactory(), NormalStrategy()),
                                            (HealingCreatureFactory(),
                                             DefensiveStrategy()),
                                            (TransformCreatureFactory(),
                                                AggressiveStrategy())])
