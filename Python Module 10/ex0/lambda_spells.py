def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda x: x['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (list(filter(lambda x: x['power'] >= min_power, mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda name:  f"* {name} *", spells)))


def mage_stats(mages: list[dict]) -> dict:

    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    powers = list(map(lambda mage: mage['power'], mages))
    avg_power = sum(powers) / len(mages)

    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': round(avg_power, 2)
    }


def artifacts() -> None:

    fireball = {
        "name": "fireball",
        "power": 92,
        "type": "Fire Staff"
    }

    heal = {
        "name": "heal",
        "power": 85,
        "type": "Crystal Orb"
    }

    shield = {
        "name": "shield",
        "power": 57,
        "type": "Magic Iron"
    }

    objects = [heal, fireball, shield]

    print("===ARTEFACTS===\n")

    print("Testing artifact sorter ...")
    sorted_objects = artifact_sorter(objects)
    print("Artifacts without sorting: "
          f"{[f"{i['name']} ({i['power']})" for i in objects]}")
    print("Sorted artifacts: "
          f"{[f"{i['name']} ({i['power']})" for i in sorted_objects]}")

    # Here the list with the sorted names is
    # created with the list comprehension
    sorted_names = [item['name'] for item in sorted_objects]

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(sorted_names)))


def mages() -> None:

    maestre = {
        "name": "Maestre",
        "power": 754,
        "element": "fire"
    }

    kirus = {
        "name": "Kirus",
        "power": 120,
        "element": "water"
    }

    gandalf = {
        "name": "gandalf",
        "power": 981,
        "element": "light"
    }

    mages = [maestre, kirus, gandalf]

    print("\n===MAGES===\n")

    filtered_mages = power_filter(mages, 500)
    print("Mages without filtering: "
          f"{[f"{i['name']} ({i['power']})" for i in mages]}")
    print(f"Filtered mages: "
          f"{[f"{i['name']} ({i['power']})" for i in filtered_mages]}\n")

    print(f"Mage stats: {mage_stats(mages)}")


if __name__ == "__main__":

    artifacts()
    mages()
