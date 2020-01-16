#!/usr/bin/python3
# Changing variables

x = "hi"
def read_x():
	print(x)
def change_local_x():
	x ="bye"
	print(x)
def change_global_x():
	global x
	x = "aloha"
	print(x)


read_x()
change_local_x()
print(x)
change_global_x()
read_x()


