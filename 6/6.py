sumOfSq = 0
sqOfSum = 0
for i in range(100):
    sumOfSq += (i+1) ** 2
    sqOfSum += (i+1)

sqOfSum = sqOfSum ** 2
diff = sqOfSum - sumOfSq
print(diff)