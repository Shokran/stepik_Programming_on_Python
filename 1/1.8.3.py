x = int(input())
h = int(input())
m = int(input())
print((h + x // 60) + ((m + x % 60) // 60))
print((m + x % 60) % 60)

# ((a and (b or (not a))) and (not b))
# ((a and b) or ((not a) and (not b)))

x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)
