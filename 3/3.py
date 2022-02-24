from itertools import count


NUMBER = 600851475143
numTemp = NUMBER
largestFactor = 0
Counter = 2

while numTemp != 1:
    if numTemp % Counter == 0:
        numTemp /= Counter
        largestFactor, Counter = Counter, 2
    else:
        Counter += 1

print(largestFactor)