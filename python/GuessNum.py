from random import randint

user_input = ''
x = random.randint(1,10)
print("The random number is between 1-10")

while user_input != x:
	user_input =int(input("Guess the number between 1-10:"))
	if user_input > x:
		print("Too High, try again")
	if user_input < x:
		print("Too Low, try again")
	if user_input == x:
		print("Congratulations")
		break


