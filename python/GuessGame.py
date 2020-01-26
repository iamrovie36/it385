#!/usr/bin/python3

# Guessing Game

import random

print("Hello please pick a maximum number to guess:")
MaxNum = int(input())

Num = random.randint(1,MaxNum)

print("Please take a guess between 1 and the number you choose:")
guess = int(input())

while guess != Num:
	if Num < guess:
		print("Your guess was too high please guess again:")
		guess = int(input())

	elif Num > guess:
		print("Your guess was too low please guess again:")
		guess = int(input())

if guess == Num:
	print("You guess correct!")
