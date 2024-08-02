# Dice Game Rules
# - Players take turns rolling the dice.
# - On each turn, a player can roll the dice multiple times.
# - If a player rolls a 1, their turn ends and no points are added to their total for that turn.
# - If a player chooses to stop rolling before rolling a 1, the sum of their rolls is added to their total score.
# - The first player to reach 50 points wins the game.
import random

def roll():
	num = random.randint(1, 6)
	return num

def display_current_scores(my_list):
	count = 1
	for i in my_list:
		print(f"Player {count} has {i} points")
		count += 1

while True:
	playercount = input("Enter the number of players(1 - 4):")
	if playercount.isdigit():
		playercount = int(playercount)
		if (playercount >= 1 and playercount <= 4):
			break
	print("Please enter a valid number")

max_score = 50
player_scores = [0 for _ in range(playercount)]

while True and max_score > max(player_scores):
	temp_scores = [0 for _ in range(playercount)]
	display_current_scores(player_scores)
	print("\n")
	for i in range(0,playercount):
		if not(max_score > max(player_scores) and max_score > max(temp_scores)):
			break
		while True and max_score > max(player_scores) and max_score > max(temp_scores):
			print("Player ", i + 1, "are you ready? We are rolling lets see your luck now")
			value = roll()
			if (value == 1):
				print("It seems like you ran out of luck buddy you got 1\n")
				temp_scores[i] = 0
				break
			print("Yay!! you rolled ",value)
			temp_scores[i] += value
			print("Your current score is ",temp_scores[i],"\nWould you like to add it to the grand total?(y / n)")
			if input().lower() == 'y':
				player_scores[i] += temp_scores[i]
				print("\n")
				break
			print("Let's roll it again\n\n")
winner = player_scores.index(max(player_scores)) + 1
print(f"Player {winner+1} has won the game and has become the unbeatable gambler as for the others I would just say better luck next time")
