import math


def len_simulator(a) -> int:
    i = 0
    for char in a:
        i += 1
    return i


def floater_and_tupler(split_coordinates) -> tuple[float, float, float]:
    i = 0
    commas = 0
    length_sc = len_simulator(split_coordinates)
    temp_str = ""
    pre_floated_list: list[str] = []
    try:
        while i < length_sc:
            if commas > 2:
                raise Exception("Invalid syntax")
            if split_coordinates[i] == ',':
                pre_floated_list.append(temp_str)
                temp_str = ""
                commas += 1
            else:
                temp_str = temp_str + split_coordinates[i]
            i += 1
        pre_floated_list.append(temp_str)
        if len(pre_floated_list) != 3:
            raise Exception("Invalid syntax")
    except Exception:
        raise Exception("Invalid syntax")
    floated_list: list[float] = []
    try:
        for element in pre_floated_list:
            floated_list.append(float(element))
    except ValueError:
        raise Exception(f"Error on parameter '{element}': could not convert"
                        f" string to float: '{element}'")

    return floated_list[0], floated_list[1], floated_list[2]


def distance_between_points(point_0, sct) -> float:
    i = 0
    sume = 0
    while i < 3:
        sume = sume + (sct[i] - point_0[i])**2
        i += 1
    return round((math.sqrt(sume)), 4)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        a = input("Enter new coordinates as floats in format 'x,y,z': ")
        tuple_center = (0, 0, 0)
        try:
            sct: tuple[float, float, float] = floater_and_tupler(a)
            print(f"Got a first tuple: {sct}")
            print(f"It includes: X={sct[0]}, Y={sct[1]}, Z={sct[2]}")
            print(f"Distance to center: "
                  f"{distance_between_points(sct, tuple_center)}")
            return (sct)
        except Exception as e:
            print(f"{e}")


def second_set(point_0) -> None:
    while True:
        a = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            sct: tuple[float, float, float] = floater_and_tupler(a)
            print(f"Distance between the 2 sets of coordinates: "
                  f"{distance_between_points(point_0, sct)}")
            return
        except Exception as e:
            print(f"{e}")


def pre_pos() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_point: tuple[float, float, float] = get_player_pos()
    print()
    print("\nGet a second set of coordinates")
    second_set(first_point)


if __name__ == "__main__":
    pre_pos()
