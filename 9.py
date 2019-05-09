amount = int(input())


def get_right_amount():
    ost = amount % 100
    if 5 <= ost < 21:
        return 'ok'
    else:
        return 'ne_ok'


print(get_right_amount())

