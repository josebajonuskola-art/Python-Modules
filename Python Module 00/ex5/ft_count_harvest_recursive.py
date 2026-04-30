def ft_count_harvest_recursive():
    basecase = int(input('Days until harvest: '))

    def helper(basecase: int, days: int):
        if days <= basecase:
            print('Day ' + str(days))
            helper(basecase, days + 1)
    helper(basecase, 1)

    print('Harvest time!')
