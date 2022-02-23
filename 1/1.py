a = 0
n = 1
total = 0

while a < 1000:
    a = n * 3
    total += a
    n += 1

n = 1
while a < 1000:
    a = n * 5
    n += 1
    total += a

print(total)