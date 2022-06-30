#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arg
    if len(arg) == 1:
        print("0 arguments.")
    elif len(arg) == 2:
        print("1 argument:\n1: {}".format(arg[1]))
    else:
        print("{} arguments:".format(len(arg) - 1))
        for i in range(len(arg)):
            if i != 0:
                print("{}: {}".format(i, arg[i]))
