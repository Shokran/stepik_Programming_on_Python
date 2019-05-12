a = int(input())
b = int(input())
amount = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        amount += i
        count += 1
print(amount / count)
