# Timed Math Challenge
# - The challenge presents the user with 10 math problems to solve.
# - Each problem is randomly generated.
# - The user inputs their answer for each problem.
# - The time taken to complete all 10 problems is recorded.
# - At the end of the challenge, the total time taken is displayed.

import random
import time

OPERATORS = ["+","-","*"]
MAX_OPERANDS = 12
MIN_OPERANDS = 3
TOTAL_PROBLEMS = 10

def generate_equation():
	left = random.randint(MIN_OPERANDS,MAX_OPERANDS)
	right = random.randint(MIN_OPERANDS,MAX_OPERANDS)
	operator = random.choice(OPERATORS)
	expr = str(left)+ " " + operator + " " + str(right)
	answer = eval(expr)
	return expr, answer

wrong = 0
input("Press enter to start the challenge !!")
print("-------------------------------------")

starttime = time.time()
for i in range(TOTAL_PROBLEMS):
	expr, answer = generate_equation()
	while True:
		userans = input("What would be the answer for Problem #" + str(i+1)+ ":"+ expr+"? ")
		if(userans == str(answer)):
			break
		wrong += 1
endtime = time.time()
timetaken = round(endtime - starttime, 2)
print("-------------------------------------")
print("Nice work you finished it in",timetaken,"seconds !!")
