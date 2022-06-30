#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as Ebuka
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, Ebuka.add(a, b)))
    print("{} - {} = {}".format(a, b, Ebuka.sub(a, b)))
    print("{} * {} = {}".format(a, b, Ebuka.mul(a, b)))
    print("{} / {} = {}".format(a, b, Ebuka.div(a, b)))
