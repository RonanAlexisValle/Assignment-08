#   This python program is a number guessing name between 0-100
#   From the word itself the user will try to guess what number the program is generated.
#   Using clues like (greater than) or (Less than) will make the game easier for the user.
#   This program uses 'while', and 'if' loops.

import random
number = random.randint(0, 100)
restart = True
start = True

#STEP.1- The program will ask first the user's name, print a short welcome message, and will print the instructions of the game.
def ask_name():
    name = input("What name should I call you?\n")
    print(f"Hello {name}! Welcome to the number guessing game!")
    print("This game is just simple, all you need to do is to guess the number between 0 to 100")
    return
ask_name()

#STEP.2- The game will start by asking the user on what number is in the computer's mind.
#        Clues are provided in order for the user to guess easier. 
#        The clues will be printed according to the user's guess.
while restart:  

    while start:
        user_guess = int(input("What number is on my mind? (0-100)\n"))
        if user_guess < number:
            print("Your guess is too low! Greater than!")
        if user_guess > number:
            print("Your guess is too high! Less than!")
        if user_guess == number:
            break
#STEP.3- Once the user guess the number completely, this message will be printed out in the output console.
    if user_guess == number:        
        print("You got it correctly! Nice job!")

#STEP.4- Lastly, if the user wants to start the game again or exit the program, the commands to do so are printed out.
    restart = input("Would you like to restart the game? Press [y] if yes and [n] to dismiss.\n")
    if restart == "n":
        break
    if restart == "y":
        restart = True




