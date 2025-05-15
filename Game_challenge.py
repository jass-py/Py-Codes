# Game challenge :

# Mini Project: Guess the Secret Number

# Requirements:
"""
	1.	The program sets a secret number (e.g., 7).
	2.	The user is asked to guess the number.
	3.	If the guess is correct, print "You guessed it!"
	4.	Keep asking until they guess correctly (you’ll need a while loop).
"""

secret_number = 7

while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("You guessed it!")
        break
