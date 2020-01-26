#!/usr/bin/python3
# Script that reads a file

# easy reading of file
myFile = open("testfile.txt", "r")
print(myFile.read(5))
print(myFile.read())

# reading file line by line
myFile = open("testfile.txt", "r")
for line in myFile:
	if line.startswith("a"):
		print(line)
myFile.close()

# Read file usoing a WITH statement
with open("testfile.txt", "r") as myFile:
	print(myFile.read())

