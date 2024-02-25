while True:
    var = input("input bill or end for exit:")
    if var == "end":
        break
    bill = float(var)
    paid = float(input("input paid:"))
    change = paid - bill
    print(f'change is {change:.2f}, return as follows:')

    nominals = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    for n in nominals:
        if change // n != 0:
            print(f'{change // n} * {n}lv')
            change -= (change // n) * n
            change = round(change, 2)

# OLD VERSION
    # if change // 50 > 0:
    #     print(f'{change // 50} * 50lv')
    #     change -= (change // 50) * 50
    #     change = round(change, 2)
    #
    # if change // 20 > 0:
    #     print(f'{change // 20} * 20lv')
    #     change -= (change // 20) * 20
    #     change = round(change, 2)
    #
    # if change // 10 > 0:
    #     print(f'{change // 10} * 10lv')
    #     change -= (change // 10) * 10
    #     change = round(change, 2)
    #
    # if change // 5 > 0:
    #     print(f'{change // 5} * 10lv')
    #     change -= (change // 5) * 5
    #     change = round(change, 2)
    #
    # if change // 2 > 0:
    #     print(f'{change // 2} * 2lv')
    #     change -= (change // 2) * 2
    #     change = round(change, 2)
    #
    # if change // 1 > 0:
    #     print(f'{change // 1} * 1lv')
    #     change -= (change // 1) * 1
    #     change = round(change, 2)
    #
    # if change // 0.5 > 0:
    #     print(f'{change // 0.5} * 0.50lv')
    #     change -= (change // 0.5) * 0.50
    #     change = round(change, 2)
    #
    # if change // 0.2 > 0:
    #     print(f'{change // 0.2} * 0.20lv')
    #     change -= (change // 0.2) * 0.2
    #     change = round(change, 2)
    #
    # if change // 0.1 > 0:
    #     print(f'{change // 0.1} * 0.10lv')
    #     change -= (change // 0.1) * 0.1
    #     change = round(change, 2)
    #
    # if change // 0.05 > 0:
    #     print(f'{change // 0.05} * 0.05lv')
    #     change -= (change // 0.05) * 0.05
    #     change = round(change, 2)
    #
    # if change // 0.02 > 0:
    #     print(f'{change // 0.02} * 0.02lv')
    #     change -= (change // 0.02) * 0.02
    #     change = round(change, 2)
    #
    # if change // 0.01 > 0:
    #     print(f'{change // 0.01} * 0.01lv')
    #     change -= (change // 0.01) * 0.01
    #     change = round(change, 2)


