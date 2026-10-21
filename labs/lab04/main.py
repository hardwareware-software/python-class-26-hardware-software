# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header

import random

def display_title():
    print("Guess the Number game")
    print()

def play_game():
    print(""" 

E: Easy - guess from 1 to 10, limit 5 attempts
M: Medium - Guess 1 - 100, limit 7 attempts
H: Hard - Guess from 1 to 1000, limit 10 attempts
        """)
    your_level = input("Which level would you like to play? E/M/H:")
    # set limit based on game level choice
    if your_level.upper() == "E":
        limit = 10
        attempts= 4
    elif your_level.upper() == "M":
        limit = 100
        attempts = 5
    elif your_level.upper() == "H":
        limit = 1000
        attempts = 11
    else:
        limit = 10000 # punishment for incorrect level 

    secret_number = random.randint(1, limit)
    print(f"I am thinking of a number from 1 to {limit}\n")
    count = 1 # keep track of total number of attempts
    
    # check if they have any attempts left
        
    while (guess := int(input("Your guess: "))) != secret_number:
        if count >= attempts:
           print("Sorry, You dont have any attempts left!")
           break 
        if guess < secret_number:
            print("Sorry, you're guess too low.")
        elif guess > secret_number:
            print("Sorry, you're guess is too high.")
        count += 1 # increment the guess attempt counter
    else: # if they guessed correctly
        print(f"Congrats! You guessed it in {count} tries!\n")

def main():
    # the main program driver
    display_title()

    # ask for the players name
    player_name = input("Hi there! What is your name?")
    print()

    again = "y" # set intial game loop variable

    while again.lower() == "y": # play the game
        play_game()
        again = input(f"Would you like to play another round of the game, {player_name}? y/n:")
        print()

    print("Thanks for playing! Goodbye!")

# if started as the main module, call the main() function 
if __name__ == "__main__":
    main()
