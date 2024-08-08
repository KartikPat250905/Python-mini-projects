import random

while True:
	top_of_range = input("Enter the max number to generate:")
	if (top_of_range.isdigit()):
		break

random_number = random.randint(-int(top_of_range),int(top_of_range))
input("Are you ready the game is about to start:")
print("-----------------------------------------")
while True:
	guess = input("Enter your guess:")
	if(guess.lstrip('-').isdigit()):
		break
guess = int(guess)
if(guess > random_number):
	print("Your guess is greater than the answer")
elif(guess < random_number):
	print("Your guess is smaller than the answer")
no_of_guesses = 2
while guess != random_number:
	while True:
		guess = input("Enter your guess:")
		if(guess.lstrip('-').isdigit()):
			break
	guess = int(guess)
	if(guess == random_number):
		break
	elif(guess > random_number):
		print("Your guess is greater than the answer")
	elif(guess < random_number):
		print("Your guess is smaller than the answer")
	no_of_guesses += 1
print("Congratulations you have guessed the correct number !!")
print("It took you",no_of_guesses,"to guess the number")
print("------------------------------------------------------")
