# ask user for input
player=input("What do you choose? Rock, paper, or scissors?  ")

# determine computer's choice
import random
options= ["rock", "paper", "scissors"]
computer= random.choice(options)

print("The computer chose: " + computer)
if computer=="rock" and player=="paper":
	print("You win!")
elif computer=="rock" and player=="scissors":
	print("You lose!")
elif computer=="paper" and player=="rock":
	print("You lose!")
elif computer=="paper" and player=="scissors":
	print("You win!")
elif computer=="scissors" and player=="rock":
	print("You win!")
elif computer=="scissors" and player=="paper":
	print("You lose!")
else:
	print("There is a tie.")
