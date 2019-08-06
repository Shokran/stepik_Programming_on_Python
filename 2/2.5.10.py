a = [int(i) for i in input().split()]
b = []
for i in range(len(a)):
    if len(a) == 1:
        b = str(a[i])
    #     b.append(a[i - 1] + a[i + 1])
    # else:
    #     b.append(a[i])

print(b)
