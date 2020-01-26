#!/usr/bin/python3
# example of writing a file in Python

# Open the file
myFile = open("testfile.txt", "w")

# Write to the File
myFile.write("Hello World\n")
myFile.write("It is, it is\n")
myFile.write("a wonderful thing\n")
myFile.write("to be the Pirate King!\n")

# Close the File
myFile.close()

