import random
number = random.randint(-10000, 10000)
last_digit = a = (str(number)[-1])
if a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
if a == 0:
    print(f"Last digit of {number} is {a} and is 0")
if a < 6 and a != 0:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
