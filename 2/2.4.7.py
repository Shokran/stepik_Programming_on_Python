string = input() + ' '
count = 0

for i in string:
    if string[0] != i:
        print(string[0], count, end='', sep='')
        count = 0
        string = i
    count += 1
