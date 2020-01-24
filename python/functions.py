#!/usr/bin/python3

# Basic function
def func1():
	print("Lets get funky")

# Function that takes an argument
def addNums(val1, val2):
	print(val1 + val2)

# Function with a default value
def power(num, power = 2):
	result = 1
	for i in range(power):
		result = result * num
	print(result)

# call functions
#func1()
#print(func1())
#print(func1)

#addNums(7, 11)
#addNums(val2 = 11, val1 = 7)

power(5)
power(5,2)
power(5,3)





