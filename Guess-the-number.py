#Create a ”Guess-the-Number” game. 
#Include algorithm
#Include comments
#Make smart use of print statements and names
#User must guess a number randomly chosen by computer. Computer will tell user if it’s too high or too low and let the user try again.


## The Algorithm
#1) have computer randomly select a number from 1-20
#2) ask user for a guess
#3) determine if user's guess is too high or too low
#4) tell user if their guess is too high or too low
#5) repeat steps 2-4 until user guesses correctly
#6) tell user they guessed correctly

import random
target= random.choice(range(1,21))

player=int(input("The computer will select a number from 1-20 \nGuess the number\n")) #must convert string to integer for loop to evaluate properly.

while player != target:
        if player > target:
                print("Too high!")
                player=int(input("Guess again. \n"))
        else:
                print("Too low!")
                player=int(input("Guess again. \n"))
else:
        print("You got it!")

