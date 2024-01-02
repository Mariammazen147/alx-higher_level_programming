#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = int(repr(number)[-1])
if number < 0:
    ld *= -1
if ld == 0:
    print("Last digit of {:d} is {:d} and is zero".format(number, ld))
elif abs(ld) < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, ld))
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, ld))
