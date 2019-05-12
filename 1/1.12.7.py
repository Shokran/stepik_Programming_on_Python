number = str(input())


def lucky_number():
    if len(number) == 6:
        first = number[:len(number) // 2]
        second = number[len(number) // 2:]
        sum_first = int(first[0]) + int(first[1]) + int(first[2])
        sum_second = int(second[0]) + int(second[1]) + int(second[2])
        if sum_first == sum_second:
            return "Счастливый"
        else:
            return "Обычный"
    else:
        return "Неверный ввод"


print(lucky_number())
