genome = input().upper()
gc = 0

for guacit in genome:
    if guacit == 'G' or guacit == 'C':
        gc += 1

print((gc / len(genome)) * 100)
