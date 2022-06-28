#!/usr/bin/python3
for v in range(97, 123):
    if v == 113 or v == 101:
        continue
    print(f"{v:c}", end="")
