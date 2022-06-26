if __name__ == "__main__":
    for a in range(1, 333):
        for b in range(2, 499):
            for c in range(3, 997):
                if (a < b < c) and (a + b + c == 1000) and (a ** 2 + b ** 2 == c ** 2):
                    print(a)
                    print(b)
                    print(c)