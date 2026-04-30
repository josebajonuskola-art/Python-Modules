import random


def achievement_insertor(achievements) -> set[str]:
    random_number = random.randint(5, 10)
    new_set = set(random.sample(achievements, random_number))
    return new_set


def all_achievements(alice, bob, dylan, charlie) -> None:
    all_achievements = alice.union(bob, dylan, charlie)
    print(f"All distinct achievements: {all_achievements}\n")


def intersection_finder(alice, bob, dylan, charlie) -> None:
    common_achievements = alice.intersection(bob, dylan, charlie)
    print(f"Common achievements: {common_achievements}\n")


def diff_finder(alice, bob, dylan, charlie) -> None:
    alice_diff = alice.difference(bob, dylan, charlie)
    bob_diff = bob.difference(alice, dylan, charlie)
    dylan_diff = dylan.difference(alice, bob, charlie)
    charlie_diff = charlie.difference(alice, bob, dylan)
    print(f"Only Alice has: {alice_diff}")
    print(f"Only Bob has: {bob_diff}")
    print(f"Only Dylan has: {dylan_diff}")
    print(f"Only Charlie has: {charlie_diff}\n")


def missing_finder(alice, bob, dylan, charlie, achievements) -> None:
    set_achievements = set(achievements)
    alice_missing = set_achievements.difference(alice)
    bob_missing = set_achievements.difference(bob)
    dylan_missing = set_achievements.difference(dylan)
    charlie_missing = set_achievements.difference(charlie)
    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Dylan is missing: {dylan_missing}")
    print(f"Charlie is missing: {charlie_missing}")


def gen_player_achievements() -> None:
    achievements = ["First Steps", "Survivor", "Speed Runner",
                    "Master Explorer", "Treasure Hunter", "Boss Slayer",
                    "World Savior", "Crafting Genius", "Collector Supreme",
                    "Unstoppable", "Untouchable", "Strategist",
                    "Sharp Mind", "Hidden Path Finder", "Dungeon Master",
                    "Legendary Hero", "Puzzle Solver", "Beast Tamer",
                    "Arena Champion", "Stealth Master"]
    alice = achievement_insertor(achievements)
    print(f"Player Alice: {alice}")
    bob = achievement_insertor(achievements)
    print(f"Player Bob: {bob}")
    charlie = achievement_insertor(achievements)
    print(f"Player Charlie: {charlie}")
    dylan = achievement_insertor(achievements)
    print(f"Player Dylan: {dylan}\n")
    all_achievements(alice, bob, dylan, charlie)
    intersection_finder(alice, bob, dylan, charlie)
    diff_finder(alice, bob, dylan, charlie)
    missing_finder(alice, bob, dylan, charlie, achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
