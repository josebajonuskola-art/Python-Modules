import sys


class MyRigurousError(Exception):
    def __init__(self, message=None) -> None:
        if message is None:
            self.message = "Strange error"
        else:
            self.message = message

    def __str__(self) -> str:
        return self.message


def dict_perc(inventory, total_val) -> None:
    length = len(inventory)
    i = 0
    i_l_k = list(inventory.keys())
    i_l_v = list(inventory.values())
    while i < length:
        if i_l_v[i] == 0:
            print(f"The value of '{i_l_k[i]}' must be higher than 0 ...")
        else:
            try:
                print(f"Item {i_l_k[i]} "
                      f"represents: {round(i_l_v[i] / total_val * 100, 1)}%")
            except ZeroDivisionError:
                print("Cannot be divided by zero ...")
        i += 1


def most_and_least(inventory) -> None:
    length = len(inventory)
    i_l_k = list(inventory.keys())
    i_l_v = list(inventory.values())
    i = 0
    most = i_l_v[0]
    least = i_l_v[0]
    most_i = 0
    least_i = 0
    while i < length:
        if i_l_v[i] < least:
            least = i_l_v[i]
            least_i = i
        if i_l_v[i] > most:
            most = i_l_v[i]
            most_i = i
        i += 1
    print(f"Item most abundant: {i_l_k[most_i]} with quantity {most}")
    print(f"Item least abundant: {i_l_k[least_i]} with quantity {least}")


def dictator(valid_list) -> None:
    inventory = {}
    inventory_list = []
    inventory_list = dict_valid_checker(valid_list)
    if len(inventory_list) != 0:
        for element in inventory_list:
            inventory.update({element[0]: element[1]})
    else:
        print("No items ...")
        return
    print(f"Got inventory: {inventory}")
    keys = []
    for key in inventory.keys():
        keys += [key]
    print(f"Item list: {keys}")
    total_val = 0
    for value in inventory.values():
        total_val += value
    print(f"Total quantity of"
          f" the {len(inventory.values())} items: {total_val}")
    dict_perc(inventory, total_val)
    most_and_least(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def dict_valid_checker(valid_list) -> list:
    i = 0
    split_list = []
    final_list = []
    while i < len(valid_list):
        splited = valid_list[i].split(":")
        if len(splited) != 2 or splited[1] == '':
            print(f"Error - invalid parameter '{valid_list[i]}'")
            valid_list.pop(i)
        elif splited[0] in split_list:
            print(f"Redundant item '{splited[0]}' - discarding")
            valid_list.pop(i)
        else:
            try:
                if int(splited[1]) <= 0:
                    raise MyRigurousError(f"Invalid numerical item value "
                                          f"{splited[1]} for item {splited[0]}"
                                          f" ...\nValue must be higher than 0")
                int(splited[1])
                split_list.append(splited[0])
                i += 1
            except MyRigurousError as e:
                print(f"{e}")
                valid_list.pop(i)
            except ValueError:
                print(f"Quantity error for '{splited[0]}': invalid literal "
                      f"for int() with base 10: '{splited[1]}'")
                valid_list.pop(i)
    for element in valid_list:
        splited = element.split(":")
        splited[1] = int(splited[1])
        final_list.append(splited)
    return final_list


def rpg_arguments() -> None:
    if len(sys.argv) < 2:
        print("No items provided. Usage: python3 ", end='')
        print("ft_inventory_system.py <item 1: quantity> ", end="")
        print("<item 2: quantity> ...")
        return
    print("=== Inventory System Analysis ===")
    dictator(sys.argv[1:])


if __name__ == "__main__":
    rpg_arguments()
