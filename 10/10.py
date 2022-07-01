from math import sqrt
import math

from numpy import true_divide
def ten():

    sum = 2
    primes = [2]
    for num in range(3, 2000000):
        highestInt = math.floor(math.sqrt(num))
        if checkAllPrimes(primes, highestInt, num) == True:
            primes.append(num)
            print(num)
            sum += num

    return sum

def checkAllPrimes(primes, toNum, num):
    for i in primes:
        if i > toNum:
            return True
        elif num % i == 0:
            return False
    
    return True

print(ten())