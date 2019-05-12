a = int(input())
b = int(input())
c = int(input())
d = int(input())

if 0 < a <= 10 \
        and 0 < b <= 10 \
        and 0 < c <= 10 \
        and 0 < d <= 10:
    if a <= b and c <= d:
        print(' ' + '\t', end='')
        for l in range(c, d + 1):
            print(str(l) + '\t', end='')
        print()

        for i in range(a, b + 1):
            print(str(i) + '\t', end='')
            for j in range(c, d + 1):
                print(str(i * j), end='\t')
            print()
    else:
        print("Неверный ввод")
else:
    print("Неверный ввод")
