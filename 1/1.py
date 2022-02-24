total = 0

for i in range (998):
    if (i+1) % 3 == 0 or (i+1) % 5 == 0:
        total += (i+1)

print (total)