import random


def dict_comprehension(full_cap_list) -> None:
    dictionary = {}
    sumer = 0
    high_dictionary = {}
    dictionary = {name: random.randint(54, 907) for name in full_cap_list}
    print(f"Score dict: {dictionary}")
    for element in dictionary.values():
        sumer += element
    average = round(sumer / len(full_cap_list), 2)
    print(f"Score average is {average}")
    high_dictionary = {name: score for name, score in dictionary.items()
                       if score > average}
    print(f"High scores: {high_dictionary}")


def list_comprehension_cap(initial_list) -> None:
    full_cap_list = []
    only_cap_list = []
    full_cap_list = [string.capitalize() for string in initial_list]
    print(f"New list with all names capitalized: {full_cap_list}")
    only_cap_list = [string for string in initial_list if string.istitle()]
    print(f"New list of capitalized names only: {only_cap_list}\n")
    dict_comprehension(full_cap_list)


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
                    'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_list}")
    list_comprehension_cap(initial_list)


if __name__ == "__main__":
    ft_data_alchemist()
