a = int(input())
b = int(input())
i = min(a, b)

if a and b > 0:
    while True:
        if i % a == 0 and i % b == 0:
            break
        i += 1
    print(i)
else:
    print("Не верный ввод")
