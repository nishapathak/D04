#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

guesscount = 0
print('I have picked a number between 1 & 25. Can you guess what it is? You have 5 total guesses.')

number = random.randint(1, 25)

while guesscount < 5: 
	guess = int(input())
	guesscount += 1 

	if guess == number:
		print ('Good job! You guessed my number.')
		break
	if guess < number:
		print ('Your number is too low. Try again.')
	if guess > number:
		print ('Your number is too high. Try again.')

print('Sorry, game over. I was thinking of ' + str(number) + ".")
################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()