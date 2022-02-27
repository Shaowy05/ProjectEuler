isDivisible = False
number = 20
while isDivisible == False:
    if number % 20 == 0:
        if number % 18 == 0:
            if number % 16 == 0:
                if number % 15 == 0:
                    if number % 14 == 0:
                        if number % 12 == 0:
                            print(number * 11 * 13 * 17 * 19)
                            isDivisible = True

    number += 1