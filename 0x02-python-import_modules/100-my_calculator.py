#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as ex
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} {} {} = {}".format(a, argv[2], b, ex.add(b, a)))
        elif argv[2] == "-":
            print("{} {} {} = {}".format(a, argv[2], b, ex.sub(b, a)))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(a, argv[2], b, ex.mul(b, a)))
        elif argv[2] == "/":
            print("{} {} {} = {}".format(a, argv[2], b, ex.div(b, a)))
        exit(0)
