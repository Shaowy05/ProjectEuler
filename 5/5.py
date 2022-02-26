class number:
    def factorise(self):
        listOfFactors = []
        factor = 2
        tempValue = self.value
        while factor != tempValue:
            if tempValue % factor == 0:
                listOfFactors.append(factor)
                tempValue, factor = (tempValue / factor), 2
            else:
                factor += 1
        listOfFactors.append(factor)

        tupleListOfFactors = []
        currentFactor = 2
        factorCount = 0
        for factor in listOfFactors:
            if currentFactor == factor:
                factorCount += 1
            else:
                tupleListOfFactors.append((currentFactor, factorCount))
                factorCount = 1
                while currentFactor != factor:
                    currentFactor += 1

        tupleListOfFactors.append((currentFactor, factorCount))
        
        return tupleListOfFactors

    def __init__(self, value) -> None:
        self.value = value
        self.factors = self.factorise()

def main():
    numbers = []
    for i in range(19):
        tempnumber = number((i+2))
        numbers.append(tempnumber)

    masterTupleFactors = []

    for num in numbers:
        for factor in num.factors:
            found = False
            for masterFactor in masterTupleFactors:
                if factor[0] == masterFactor[0]:
                    if factor[1] > masterFactor[1]:
                        masterFactor = factor
                    found = True
            
            if found == False:
                masterTupleFactors.append(factor)
    
    product = 1
    for factortuple in masterTupleFactors:
        product *= factortuple[0] ** factortuple[1]

    print(product)
    
main()