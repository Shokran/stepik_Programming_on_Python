amount = int(input())
programmer = " программист"


def print_phrase():
    if amount >= 0:
        remains = amount % 100
        if 5 <= remains < 21:
            ending = "ов"
            return str(amount) + programmer + ending
        else:
            remains = amount % 10
            if remains == 1:
                return str(amount) + programmer
            elif 2 <= remains <= 4:
                ending = "а"
                return str(amount) + programmer + ending
            else:
                ending = "ов"
                return str(amount) + programmer + ending

    else:
        return "Неверный ввод"


print(print_phrase())
