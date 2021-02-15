from ascii_art import logo, winner, loser
from random import randint
# from replit import clear     # if using repl.it
import os                      # if using Windows

ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5


def choose_modus():
    """ set the number of allowed guesses and return a label, depending on the modus chosen by the player """
    while True:
        player_choice = input("Type 'easy' for the easy modus or 'hard' for the hard modus of the game:\n")
        if player_choice.lower() == 'easy':
            return ATTEMPTS_EASY, "easy modus"
        elif player_choice.lower() == 'hard':
            return ATTEMPTS_HARD, "hard modus"
        else:
            print("Invalid input! -->")


def check_the_guess(guessed_number, number_to_guess, attempts_left):
    """ compare the player's guess with the random number to be guessed, provide a feedback """
    if guessed_number == number_to_guess:
        return True
    else:
        if guessed_number > number_to_guess:
            print("Your number is too high!", end="")
        elif guessed_number < number_to_guess:
            print("Your number is too low!", end="")
    
        if attempts_left > 0:
            print(" Try it again!")
            print(f"\tAttempts left: {attempts_left} ...")
            return False
        else:  
            print(f"\n\tAttempts left: {attempts_left} ...")
            return True


def play_the_game():
    """ implement the procedural structure resp. the functional logic of the game """

    # Logo + Introduction
    print(logo)
    print("\nWelcome to the fabulous game 'Guess the Number'!")
    print("\nHOW IT WORKS: The computer processing this program will generate a\n"
          "random number between 1 and 100, and the player will have a defined\n"
          "number of attempts to guess this random number.")
    print("--------------------------------------")

    # Choice of the modus
    print("\nPlease choose your preferred level of difficulty first!")
    attempts = choose_modus()[0]
    modus = choose_modus()[1]

    print("--------------------------------------")
    print(f"\nThank you! You have decided to choose the '{modus}' of the game.")
    print(f"Therefore, you will get {attempts} attempts to guess the random number.\n")

    # Start of the game
    number_to_guess = randint(1, 100)
    numbers_guessed = []
    attempts_left = attempts
    
    game_over = False
    while not game_over:
    
        confirmed = False
        while not confirmed:
            try:
                guessed_number = int(input("Make a guess: "))
                confirmed = True
            except ValueError:
                print("Invalid input! You have to enter an integer here!")

        if guessed_number in numbers_guessed:
            print("You have already guessed this number. Try another one!")
        else:
            numbers_guessed.append(guessed_number)
            attempts_left -= 1

        game_over = check_the_guess(guessed_number, number_to_guess, attempts_left)

    # End of the game / Evaluation
    print("--------------------------------------")
    if not guessed_number == number_to_guess:
        print("Too bad! You didn't make it!")
        print(f"The number to be guessed was {number_to_guess}, you have exhausted all your {attempts} attempts.")
        print(loser)
    else:
        print("Congratulations! You've got the number!")
        print(f"The number to be guessed was {number_to_guess}, you needed {attempts - attempts_left} attempt/s.")
        print(winner)

    # Restart - or quit
    confirmed = False
    while not confirmed:
        player_choice = input("Restart the game? Enter 'yes'/'y' or 'no'/'n': ")
        if player_choice.lower() == 'yes' or player_choice.lower() == 'y':
            confirmed = True
            # clear()                # if using repl.it
            # printf '\33c\e[3J'     # if using MacOS X
            os.system('cls')         # if using Windows
            play_the_game()
        elif player_choice.lower() == 'no' or player_choice.lower() == 'n':
            print("Goodbye!")
            confirmed = True
        else:
            print("Invalid input! -->")


play_the_game()
