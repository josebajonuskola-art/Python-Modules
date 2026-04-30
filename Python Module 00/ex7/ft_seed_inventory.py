def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (seed_type != "tomato" and seed_type != "carrot"
            and seed_type != "lettuce"):
        print('Unknown unit type')
    else:
        t = seed_type.capitalize()
        print(t + ' seeds: ', end='')
        if unit == 'packets':
            print(str(quantity) + ' packets available')
        elif unit == 'grams':
            print(str(quantity) + ' grams total')
        elif unit == 'area':
            print(f"covers {quantity} square meters")
            # with the 'f' all the variables are casted to type 'str' #
