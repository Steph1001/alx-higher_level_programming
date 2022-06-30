#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as ex
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        a = int(argv[1])
        b = int(argv[3])
        match argv[2]:
            case "+":
                print("{} + {} = {}".format(a, b, ex.add(b, a)))
            case "-":
                print("{} - {} = {}".format(a, b, ex.sub(b, a)))
            case "*":
                print("{} * {} = {}".format(a, b, ex.mul(b, a)))
            case "/":
                print("{} / {} = {}".format(a, b, ex.div(b, a)))
