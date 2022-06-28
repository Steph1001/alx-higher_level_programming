#!/usr/bin/python3
for char in range(26):
    if char == 4 or char == 16:
        continue
    print("{:s}".format(chr(char + ord("a"))), end="")
