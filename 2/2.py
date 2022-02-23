class num:
    def __init__(self, value, parity):
        self.value = value
        self.parity = parity

def main():
    firstNum = num(1, False)
    secondNum = num(2, True)
    total = 2

    while secondNum.value < 4000000:
        firstNum.parity, secondNum.parity = secondNum.parity, firstNum.parity

        if firstNum.parity != secondNum.parity:
            secondNum.parity = False
        else:
            secondNum.parity = True

        firstNum.value, secondNum.value = secondNum.value, firstNum.value + secondNum.value
        if secondNum.parity == True:
            total += secondNum.value

    print(total)

if __name__ == "__main__":
    main()