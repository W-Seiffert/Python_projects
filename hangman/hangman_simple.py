#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hangman_words import wordlist_DE, wordlist_EN, wordlist_IT
from hangman_art import logo, start_graphic, stages_easy, stages_hard, winner, loser
import random
import os


LETTERS = "abcdefghijklmnopqrstuvwxyzßABCDEFGHIJKLMNOPQRSTUVWXYZ"


def introduce_the_game():
    """ Introduce briefly the object and the rules of the game as well as
    the specifics of this 'hangman' program. """
    print(" _____________________________________________________________________________ \n"
          "|                                                                             |\n"
          "| Welcome to yet another command line implementation of 'Hangman', perhaps    |\n"
          "| the most popular 'word guessing' game all over the globe. As you probably   |\n"
          "| know, its object is to guess within a limited number of attempts a secret   |\n"
          "| word - either chosen randomly by the computer from a predefined list or     |\n"
          "| provided by a player, if two or more persons compete against each other.    |\n"
          "|                                                                             |\n"
          "| When the game starts, this secret word is represented in the console by a   |\n"
          "| row of dashes. Now, when the player guesses a letter that is in the word,   |\n"
          "| at each position of the word where it occurs the dash is replaced by this   |\n"
          "| letter - and he may confidently go on playing.                              |\n"
          "| However, when the player guesses a letter that is NOT in the word, this     |\n"
          "| means he comes a step closer to his virtual 'execution' - symbolized by     |\n"
          "| the addition of another element of a stick figure to the gallows drawn on   |\n"
          "| the screen after each guess.                                                |\n"
          "|                                                                             |\n"
          "| The game ends (a) if the player succeeded in guessing the word with the     |\n"
          "| allowed number of attempts, or (b) if the player has used all attempts      |\n"
          "| without guessing the word, and, thus, the 'hangman' - the stick figure      |\n"
          "| hanging on the gallows - is complete.                                       |\n"
          "|_____________________________________________________________________________|\n")

    enter_pressed = input("(--> Press ENTER to continue!)")

    player_choice = input("-- NOTE: In this rather primitive implementation of the game it is\n"
                          "         only possible to play against the computer - that is to\n"
                          "         say, it is the computer that provides all words to guess!\n"
                          "         The program is, however, shipped with wordlists in three\n"
                          "         languages (ENGLISH / GERMAN / ITALIAN, s. hangman_words.py)\n"
                          "         and leaves at least the wordlist choice to the player.\n"
                          "\n"
                          "-- For further information regarding some specifics of the program\n"
                          "   (essentially the handling of selected German and Italian special\n"
                          "   characters), please enter '1' below.\n"
                          "-- If you think you will figure out these just by playing and want\n"
                          "   directly to head over to the game, press the ENTER key!\n")

    if player_choice == "1":
        print("  -- -->\n"
              "  SOME FURTHER INFORMATION\n"
              "  ========================\n"
              "\n"
              "   (1) In order to simplify the game a little bit and in particular to ease the handling\n"
              "       of Italian accented vowels (à, è, ì, ò, ù) and of German umlauts (ä, ö, ü), a rather\n"
              "       primitive way of evaluating these has been implemented: if the word to guess contains\n"
              "       one of these special characters, the player must not type in them as vowel graphemes\n"
              "       on their own, but has to enter just the 'most closely related' vowel as defined in\n"
              "       the following lines.\n"
              "       The conventions used here (regarding the comparison of player inputs with the letters\n"
              "       of the word to guess) are as follows:\n"
              "         - the letter 'a' covers also an 'ä' in a German or an 'à' in an Italian word;\n"
              "         - the letter 'e' covers also an 'è' in an Italian word;\n"
              "         - the letter 'i' covers also an 'ì' in an Italien word;\n"
              "         - the letter 'o' covers also an 'ö' in a German or an 'ò' in an Italian word;\n"
              "         - the letter 'u' covers also an 'ü' in a German or an 'ù' in an Italian word.\n"
              "       Note: on the screen of your console, the correct graphemes of the words to guess - as\n"
              "       they are stored in the program's wordlists - will be displayed.\n"
              "   (2) Based on an analogue method of character evaluation/substitution, letters guessed\n"
              "       correctly by the player will, where needed, be converted into capitals in the display.\n"
              "       - Remember that all German nouns start with a capital!\n"
              "   (3) Repeated guesses of a letter will not be penalised here - that is, the player who\n"
              "       commits a repetition of this sort, will not lose yet another life, but just get a\n"
              "       short note making him aware of the repetition.\n"
              "  <-- --\n")

        enter_pressed = input("  --> Press ENTER to continue - and to start the game!")


def choose_wordlist():
    """ Depending on the language the player selects, return one of the wordlists of 
    the file 'hangman_words.py' from which the word to be guessed will be chosen. """
    print("(A)")
    print("\nPlease choose the language for the wordlist you prefer:")
    print("--- enter 1 for the program's English wordlist")
    print("--- enter 2 for the program's German wordlist")
    print("--- enter 3 for the program's Italian wordlist")
    while True:
        try:
            player_choice = int(input("\nYour choice: "))
            if player_choice == 1:
                wordlist = wordlist_EN
                print("All right, you will have to guess an ENGLISH word.\n")
                return wordlist
            elif player_choice == 2:
                wordlist = wordlist_DE
                print("All right, you will have to guess a GERMAN word.\n")
                return wordlist
            elif player_choice == 3:
                wordlist = wordlist_IT
                print("All right, you will have to guess an ITALIAN word.\n")
                return wordlist
            else:
                print("Invalid input! Enter 1, 2 or 3! -->")
        except ValueError:
            print("Invalid input! Enter 1, 2 or 3! -->")


def choose_level():
    """ Depending on the player's choice of a game modus, return the corresponding
    number of 'lives'/guesses and the ASCII graphic to display the gallows. """
    print("(B)")
    print("Please choose a difficulty level for the game!\n"
          "In the 'easy mode' you will have 10 attempts, in the 'hard mode' only\n" 
          "6 attempts to guess the word.")
    while True:
        try:
            level_choice = int(input("--> Enter 1 for the 'easy' mode or 2 for the 'hard' mode: "))
            if level_choice == 1:
                return 10, stages_easy
            elif level_choice == 2:
                return 6, stages_hard
            else:
                print("Invalid input! -->")
        except ValueError:
            print("Invalid input! -->")


def validate_input():
    """ Ask the player for a letter, validate the input, and - if it is valid -
    return it. """
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in LETTERS and len(guess) == 1:
            return guess
        elif len(guess) > 1:
            print("Invalid input! You have to enter exactly one character! -->")
        elif guess.lower() in ["ä", "ö", "ü", "à", "è", "ì", "ò", "ù"]:
            print("You have entered a special character that is, however, not allowed\n"
                  "as input here, but handled in a very simplified manner:\n"
                  "  enter 'a' to cover 'a'/'ä'/'à', enter 'e' to cover 'e'/'è',\n"
                  "  enter 'i' to cover 'i'/'ì', enter 'o' to cover 'o'/'ö'/'ò',\n"
                  "  enter 'u' to cover 'u'/'ü'/'ù'!\n"
                  "  -->")
        else:
            print("Invalid input! You have to enter one of the letters\n"
                  "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-ß!\n"
                  "-->")


def restart_game():
    """ Depending on the player's choice, restart or quit the game. """
    valid_choice = False
    while not valid_choice:        
        player_choice = input("Do you want to play again? (Y / N) - ")
        if player_choice.lower() == "y":
            valid_choice = True
            os.system("cls")
            # printf '\33c\e[3J'    # if using MacOS X
            play()
        elif player_choice.lower() == "n":
            valid_choice = True
        else:
            print("Invalid input! - You have to enter Y or N!")


def play():
    """ Implement the functional logic of the game, control the game flow,
    provide the obligatory 'game loop'. """

    # clear the screen, print the game's ASCII logo
    os.system("cls")
    # printf '\33c\e[3J'    # if using MacOS X
    print(logo)
    print()

    introduce_the_game()

    # clear the screen again
    os.system("cls")
    # printf '\33c\e[3J'    # if using MacOS X

    print("\n========================================================================\n")
    print("\t*** GAME SETTINGS ***\n")

    # let the program create a random word, based on a wordlist chosen by the player
    wordlist = choose_wordlist()
    chosen_word = random.choice(wordlist)

    # create a new variable to store a modified version of the word to guess - a version that allows
    # the program to compare without further efforts the letters of this word with those guessed by
    # the player (>< Note: the special characters of some Italian and German words should be ignored
    # in the comparison and thus simply replaced by their "nearest relatives", but, on the other hand,
    # should be displayed in the player's answer as well as the list of letters that have already been
    # guessed (see below)!)
    chosen_word_to_check = chosen_word.lower()
    chosen_word_to_check = chosen_word_to_check.replace("ä", "a").replace("ö", "o").replace("ü", "u")
    chosen_word_to_check = chosen_word_to_check.replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u")

    # prepare the display of the word to be guessed
    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"

    # let the player choose one of the game's two difficulty levels
    print()
    lives, stages = choose_level()
    nr_of_guesses = lives
    print()

    # provide a list to which all letters guessed during the game will be added
    guessed_letters = []

    # clear the screen again, print a "start" graphic, and let the player guess
    os.system("cls")
    # printf '\33c\e[3J'    # if using MacOS X
    print(start_graphic)

    # start of the "game loop" (!)
    end_of_game = False
    while not end_of_game:

        # ask the player for a guess
        guess = validate_input()

        # clear the screen again, evaluate the player's guess
        os.system("cls")
        # printf '\33c\e[3J'    # if using MacOS X
        print("*   * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *   *")
        print("* * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *\n")

        # special handling for the repeated guess of a letter
        if guess in guessed_letters:
            print(f"FYI: You have already guessed the letter '{guess}'!")

        # case 1: the letter guessed by the player is in the word to guess
        elif guess in chosen_word_to_check:
            for position in range(word_length):
                letter = chosen_word_to_check[position]
                if letter == guess:
                    display[position] = chosen_word[position]
            guessed_letters.append(guess)

        # case 2: the letter guessed by the player is not in the word to guess
        elif guess not in chosen_word_to_check:
            print(f"The letter '{guess}' is not in the word!\nYou lose a life! :^(")
            guessed_letters.append(guess)
            lives -= 1
            # end of the game, scenario 1: the player did not guess the word
            if lives == 0:
                end_of_game = True
                print(loser)
                print(f"\nOuch, that was number {nr_of_guesses}!\nGAME OVER! You did not make it!")
                print(":'-(")
                print(f"--- The word to be guessed was '{chosen_word}'!\n")

        # display of the word to be guessed
        print(f"{' '.join(display)}")

        # end of the game, scenario 2: the player guessed the word
        if "_" not in display:
            end_of_game = True
            print(winner)
            print("\nCONGRATULATIONS! - You have guessed the word!")
            print(":-D")

        # display of the gallows and the list of guessed letters
        print(stages[lives])
        print("\t\tyour inputs: ", end="")
        print(len(guessed_letters), end =" ")
        print(f"(<-- guessed wrong: {nr_of_guesses - lives})")
        print("\t\t", end="")
        print(guessed_letters)
        print()

    restart_game()

play()
