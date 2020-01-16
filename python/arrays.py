#!/usr/bin/python3
# Demonstrates using Arrays in Python
from array import *


my_array = array('i', [1,2,3,4,5])
print(my_array[0])
print(my_array[2])
print(my_array[-1])
print(my_array)

my_array.append(99)
my_array.insert(1,0)
print(my_array.tolist())




