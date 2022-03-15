from num import NUM
largestPr = 0

for i in range(1000):
    pr = int(NUM[i])
    for j in range(12):
        try:
            pr *= int(NUM[i+j+1])
        except:
            print(largestPr)
            break

    if pr > largestPr:
        largestPr = pr