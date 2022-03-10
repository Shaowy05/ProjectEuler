primeList = [2]
num = 3
while len(primeList) <= 10000:
    isPrime = True
    for prime in primeList:
        if num % prime == 0:
            isPrime = False
            break

    if isPrime == True:
        print(num)
        primeList.append(num)
    
    num += 2

print(primeList[10000])