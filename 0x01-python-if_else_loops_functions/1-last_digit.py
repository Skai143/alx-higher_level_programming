#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = a = (str(number)[-1])
a = int(a)
if number < 0:
    a = -a
if a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
elif a < 6 and a != 0:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {a} and is 0")
