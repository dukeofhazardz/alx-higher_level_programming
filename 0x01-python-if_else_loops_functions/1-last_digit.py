#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if (number < 0):
	print("Last digit of {0} is -{1}".format(number, lastDigit), end=' ')
else:
	print("Last digit of {0} is {1}".format(number, lastDigit), end=' ')
if (lastDigit > 5):
	print("and is greater than 5", end='\n')
elif (lastDigit == 0):
	print("and is 0", end='\n')
elif (lastDigit < 6 and lastDigit != 0):
	print("and is less than 6 and not 0", end='\n')
