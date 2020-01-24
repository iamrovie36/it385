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

# Function that retunrs a value
def cube(x):
	return x * x * x

# Function that adds variable number of numbers
def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result

# call functions
print(multi_add(6, 7))
print(multi_add(234,324, 52, 5234, 56, 2345, 234553, 23452))



#cube(3)
#print(cube(5))
#myCube = cube(42)
#print(myCube)



#func1()
#print(func1())
#print(func1)

#addNums(7, 11)
#addNums(val2 = 11, val1 = 7)

#power(5)
#power(5,2)
#power(5,3)





