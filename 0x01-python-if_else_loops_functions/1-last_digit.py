#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    temp = abs(number) % 10
    lastDigit = -temp
else:
    lastDigit = number % 10

print(f"Last digit of {number} is {lastDigit}", end=' ')
if lastDigit > 5:
    print("and is greater than 5", end='\n')
elif lastDigit == 0:
    print("and is 0", end='\n')
elif lastDigit < 6 and lastDigit != 0:
    print("and is less than 6 and not 0", end='\n')
