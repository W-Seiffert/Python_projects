#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hangman_words import wordlist_DE, wordlist_EN, wordlist_IT
from hangman_art import logo, start_graphic, stages_easy, stages_hard, winner, loser
import random
import os
import re


LETTERS = "abcdefghijklmnopqrstuvwxyzäöüàèìòùßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"


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
          "| row of dashes. When the player (or the player whose turn it is) guesses a   |\n"
          "| letter that is in the word, at each position of the word where it occurs    |\n"
          "| the dash is replaced by this letter - and he may confidently go on playing. |\n"
          "| However, when the player guesses a letter that is NOT in the word, this     |\n"
          "| means he comes a step closer to his virtual 'execution' - symbolized by     |\n"
          "| the addition of another element of a stick figure to the gallows drawn on   |\n"
          "| the screen after each guess.                                                |\n"
          "|                                                                             |\n"
          "| The game ends (a) if the player succeeded in guessing the word within the   |\n"
          "| allowed number of attempts, or (b) if the player has used all his attempts  |\n"
          "| without guessing the word, and, thus, the 'hangman' - i.e. the stick figure |\n"
          "| hanging on the gallows - is complete.                                       |\n"
          "|_____________________________________________________________________________|\n")

    enter_pressed = input("--> Press ENTER to continue!")

    print("\n** NOTE: This program allows you to play both the computer version and a\n"
          "multiplayer version of the game. In addition, it is shipped with wordlists\n"
          "in three languages (English, German, Italian), that may foster your multi-\n"
          "lingual skills while playing against the computer.\n")

    print("------------------------------------------------------------------------\n")

    player_choice = input("-- For further information regarding some specifics of the program\n"
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
              "       generous way of evaluating these has been implemented: if the word to guess contains\n"
              "       one of these special characters, the player does not have to type in them as vowel\n"
              "       graphemes on their own (although they are accepted characters!), but may just enter\n"
              "       the 'most closely related' vowel as defined in the following lines.\n"
              "       The conventions used here (regarding the comparison of player inputs with the letters\n"
              "       of the word to guess) are as follows:\n"
              "         - the letter 'a' covers also an 'ä' in a German or an 'à' in an Italian word;\n"
              "         - the letter 'e' covers also an 'è' in an Italian word;\n"
              "         - the letter 'i' covers also an 'ì' in an Italien word;\n"
              "         - the letter 'o' covers also an 'ö' in a German or an 'ò' in an Italian word;\n"
              "         - the letter 'u' covers also an 'ü' in a German or an 'ù' in an Italian word.\n"
              "       Note: on the screen of your console, the correct graphemes of the words to guess - as\n"
              "       they are stored in the program's wordlists or were passed by the players contributing\n"
              "       them - will be displayed.\n"
              "   (2) Based on an analogue method of character evaluation/substitution, letters guessed\n"
              "       correctly by the player will, where needed, be converted into capitals in the display.\n"
              "       - Remember that all German nouns start with a capital!\n"
              "   (3) Repeated guesses of a letter will not be penalised here - that is, the player who\n"
              "       commits a repetition of this sort, will not lose yet another life, but just get a\n"
              "       short note making him aware of the repetition.\n"
              "  <-- --\n")

        enter_pressed = input("  --> Press ENTER to continue!")


def get_players():
    """ Introduce the multiplayer modus of the game, return a dictionary of all players, 
    based on their required inputs, and the pair of players selected to start. 
    (--> multiplayer version) """
    print("\nOkay, you have selected the 'multiplayer version' of the game, so in\n"
          "each round one of the players will have to provide a word to guess\n"
          "- and another one will have to guess. The former will receive a point\n"
          "if his word is not guessed with the available attempts, the latter,\n"
          "on the other hand, if he succeeds in guessing it.")

    # set the number of players
    while True:
        try:
            nr_of_players = int(input("\nNow, to begin with, enter the desired number of players: "))
            break
        except ValueError:
            print("Invalid input! --> You have to enter a whole number!")

    # set names/numbers for the players
    print(f"\nAll right, the game will be arranged for {nr_of_players} players.")
    players = {}
    players_choice = input("If you want the players to be addressed by names, please enter '1' below -\n"
                          "otherwise just press the ENTER key!\n" 
                          "In this case, each player will be assigned a number! ('p1', etc.)\n")
    if players_choice == "1":
        print("Great, so please type in below a name for every player!")
        for i in range(nr_of_players):
            players_name = input(f"-- name of player {i+1}: ")
            players[players_name] = {"score": 0, "matches": 0}
    else:
        for i in range(nr_of_players):
            players[f"p{i+1}"] = {"score": 0, "matches": 0}

    word_setter = list(players)[0]
    word_guesser = list(players)[1]
    print(f"\nOkay, the players' dictionary is complete! - You are almost done.")
    print(f"\n   FYI: {word_setter} will be the first to provide a word,\n"
          f"        {word_guesser} the first to assume the role of the guesser.")
    print("   -------------------------------------------------------")

    # return the players dictionary as well as the players who will start
    return players, word_setter, word_guesser


def get_player_word(word_setter):
    """ Ask the player whose turn it is to provide a word to guess, validate his input,
    and - if it is valid - return it. 
    (--> multiplayer version) """
    os.system("cls")
    #printf '\33c\e[3J'    # if using MacOS X
    print(f"\n  All right, {word_setter}, it's your turn now! Make sure the player who will have\n"
          "  to guess your word is not in front of the screen - and then type in a word.\n")

    print("  +------------------------------------------------------------------------+")
    print("  |                                                                        |")
    print("  | NOTE: you have to enter a continuous String of at least three letters! |")
    print("  |                                                                        |")
    print("  | --> accepted characters:                                               |")
    print("  |                                                                        |")
    print("  |   a b c d e f g h i j k l m n o p q r s t u v w x y z ä ö ü à è ò ù ß  |")
    print("  |   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Ä Ö Ü            |")
    print("  |                                                                        |")
    print("  +------------------------------------------------------------------------+")
    print("\n\n")

    while True:

        players_word = input("--> Your word: ")
        if all(x in LETTERS for x in players_word) and len(players_word) >= 3:
            return players_word
        else:
            print("Invalid input! -->")


def choose_wordlist():
    """ Introduce the computer modus of the game; depending on the language the
    player selects, return one of the wordlists of the file hangman_words from
    which the word to be guessed will be chosen. 
    (--> computer version) """
    print("\nOkay, you have selected the 'computer version' of the game, so the computer\n"
          "will randomly choose words to be guessed, based on a couple of prepared\n"
          "wordlists. You will receive one point for every word you manage to guess.")
    print("\nPlease choose the language for the wordlist you prefer:")
    print("--- enter 1 for the program's English wordlist")
    print("--- enter 2 for the program's German wordlist")
    print("--- enter 3 for the program's Italian wordlist")
    while True:
        try:
            player_choice = int(input("\nYour choice: "))
            if player_choice == 1:
                wordlist = wordlist_EN
                print("All right, you will have to guess an ENGLISH word.")
                return wordlist
            elif player_choice == 2:
                wordlist = wordlist_DE
                print("All right, you will have to guess a GERMAN word.")
                return wordlist
            elif player_choice == 3:
                wordlist = wordlist_IT
                print("All right, you will have to guess an ITALIAN word.")
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
    """ Ask the player who shall guess the word for a letter, validate the input,
    and - if it is valid - return it. """
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in LETTERS and len(guess) == 1:
            return guess
        elif len(guess) > 1:
            print("Invalid input! You have to enter exactly one character! -->")
        else:
            print("Invalid input! You have to enter one of the letters\n"
                  "  a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-ä-ö-ü-ß-à-è-ì-ò-ù!\n"
                  "  -->")


def change_players(players, word_setter, word_guesser):
    """ Define the player who shall enter a new word, and the one who shall guess it.
    (--> multiplayer version) """
    print("\nOkay, so who is next? Please indicate the player who shall enter the next word!")
    print("( accepted inputs:", end=" * ")
    for player in players:
        print(player, end= " * ")
    print(")")

    while True:
        players_input = input("--> ")
        if players_input in players:
            if players_input == word_setter:
                print(f"Sorry, {word_setter} has done this job in the last round.\nPlease choose another player!")
            else:
                word_setter = players_input
                break
        else:
            print(f"Sorry, {players_input} has not been registered as a player.\n"
                  "You have to name one of the players stored in the list quoted above.")

    print("Thumbs up, your input has successfully been stored.\n" +
          f"Now, please indicate the player who shall guess {word_setter}'s word!")

    while True:
        players_input = input("--> ")
        if players_input in players:
            if players_input == word_guesser:
                print(f"Sorry, {word_guesser} has done this job in the last round.\nPlease choose another player!")
            elif players_input == word_setter:
                print(f"{word_setter} has been assigned the task to contribute the word to guess.\nPlease choose another player!")
            else:
                word_guesser = players_input
                break
        else:
            print(f"Sorry, {players_input} has not been registered as a player.\n"
                  "You have to name one of the players stored in the list quoted above.")

    print("\nExcellent, so let us head over to the next round!")

    return word_setter, word_guesser


def show_statistic_singleplayer(lives, score, rounds, all_words_so_far):
    """ Print out a current game statistic for a player of the computer version.
    (--> computer version) """
    if lives == 10:
        level = "easy"
    elif lives == 6:
        level = "hard"

    print()
    print("  GAME STATISTICS:\n")
    print("  +--------+-------+--------+")
    print("  | Rounds | Level | Points |")
    print("  |--------|-------|--------|")
    print(f"  |   {rounds:02}   | {level}  |   {score:2}   |")
    print("  +--------+-------+--------+")

    print("\n  All words that had to be guessed so far:")
    print("  ", end="")
    for i in range(len(all_words_so_far)):
        if i % 5 == 0:
            print("\n", end="  ")
        print(all_words_so_far[i], end=" / ")

    enter_pressed = input("\n\n  --> Press ENTER to continue!")


def show_statistic_multiplayer(players, lives, rounds, all_words_so_far):
    """ Print out a current game statistic for players of the multiplayer version.
    (--> multiplayer version) """
    if lives == 10:
        level = "easy"
    elif lives == 6:
        level = "hard"

    print()
    print("  GAME STATISTICS:\n")
    print("             +---------+---------+----------------+--------+")
    print("             | Points  | Matches | Rounds (total) | Level  |")
    print("  +----------|---------|---------|----------------|--------|")
    for player in players:
        print(f"  | {player:8} |    {players[player]['score']:2}   |    {players[player]['matches']:2}   |    {rounds:2}          |  {level}  |")
    print("  +----------+---------+---------+--------+----------------+")

    print("\n  All words that had to be guessed so far:")
    print("  ", end="")
    for i in range(len(all_words_so_far)):
        if i % 5 == 0:
            print("\n", end="  ")
        print(all_words_so_far[i], end=" / ")

    enter_pressed = input("\n\n  --> Press ENTER to continue!")


def get_word_modified(chosen_word):
    """ Return a modified version of the word to guess in order to enable the
    specific handling of selected German and Italian special characters, as
    sketched in the introduction. """
    chosen_word_to_check = chosen_word.lower()

    if "ä" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("ä", "ä#a")
    if "à" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("à", "à#a")
    if "è" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("è", "è#e")
    if "ì" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("ì", "ì#i")
    if "ö" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("ö", "ö#o")
    if "ò" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("ò", "ò#o")
    if "ü" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("ü", "ü#u")
    if "ù" in chosen_word_to_check:
        chosen_word_to_check = chosen_word_to_check.replace("ù", "ù#u")

    return chosen_word_to_check


def play_computer_version(wordlist, lives, stages, score, rounds, all_words_so_far):
    """ Implement the functional logic of the game's computer version, control the game flow,
    provide the obligatory 'game loop'.
    (--> computer version) """

    chosen_word = random.choice(wordlist)
    nr_of_guesses = lives

    # create a new variable to store a modified version of the word to guess,
    # that will be used to handle some Italian and German special characters
    # in the specific way intended here (as sketched in the introduction).
    chosen_word_to_check = get_word_modified(chosen_word)

    # prepare the display of the word to be guessed
    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"

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

        # special handling for repeated guesses of a letter
        if guess in guessed_letters:
            print(f"FYI: You have already guessed the letter '{guess}'!")

        # case 1: the letter guessed by the player is in the word to guess
        elif guess in chosen_word_to_check:
            if chosen_word_to_check == chosen_word.lower():
                for i in range(word_length):
                    if chosen_word_to_check[i] == guess:
                        display[i] = chosen_word[i]
            # if a special character is involved (cf. the method 'get_word_modified')
            else:
                for i in range(word_length):
                    if chosen_word.lower()[i] == guess:
                        display[i] = chosen_word[i]

                chosen_word_to_check = re.sub(".#", "", chosen_word_to_check)

                for i in range(len(chosen_word_to_check)):
                    if chosen_word_to_check[i] == guess:
                        display[i] = chosen_word[i]

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
                print(f"--- The word to be guessed was '{chosen_word}'!")

        # display of the word to be guessed
        print(f"{' '.join(display)}")

        # end of the game, scenario 2: the player guessed the word
        if "_" not in display:
            end_of_game = True
            print(winner)
            print("\nCONGRATULATIONS! - You have guessed the word!")
            print(":-D")
            score += 1

        # display of the gallows and the list of guessed letters
        print(stages[lives])
        print("\t\tyour inputs: ", end="")
        print(len(guessed_letters), end =" ")
        print(f"(<-- guessed wrong: {nr_of_guesses - lives})")
        print("\t\t", end="")
        print(guessed_letters)
        print()

    # reset / update of variables
    rounds += 1
    lives = nr_of_guesses
    all_words_so_far.append(chosen_word)

    # continuation / termination of the game
    print("\n--- CONTINUE, RESTART, OR LEAVE? ---")
    while True:
        player_choice = input("  Enter '1', if you want immediately to continue!\n"
                              "  Enter '2', if you want to get a current game statistic before!\n"
                              "  Enter '3', if you want to restart the game (to change the settings)!\n"
                              "  Enter '4', if you want to quit the game!\n"
                              "  --> Your choice: ")
        if player_choice == "1":
            play_computer_version(wordlist, lives, stages, score, rounds, all_words_so_far)
            break
        elif player_choice == "2":
            show_statistic_singleplayer(lives, score, rounds, all_words_so_far)
            play_computer_version(wordlist, lives, stages, score, rounds, all_words_so_far)
            break
        elif player_choice == "3":
            start()
            break
        elif player_choice == "4":
            print("\n  GOODBYE!")
            break
        else:
            print("Invalid input! -->")


def play_multiplayer_version(players, word_setter, word_guesser, lives, stages, rounds, all_words_so_far):
    """ Implement the functional logic of the game's multiplayer version, control the game flow,
    provide the obligatory 'game loop'.
    (--> multiplayer version) """

    chosen_word = get_player_word(word_setter)
    nr_of_guesses = lives

    # create a new variable to store a modified version of the word to guess,
    # that will be used to handle some Italian and German special characters
    # in the specific way intended here (as sketched in the introduction).
    chosen_word_to_check = get_word_modified(chosen_word)

    # prepare the display of the word to be guessed
    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"

    # provide a list to which all letters guessed during the game will be added
    guessed_letters = []

    # clear the screen again, print a "start" graphic, and let the player guess
    os.system("cls")
    # printf '\33c\e[3J'    # if using MacOS X
    print(start_graphic)

    # start of the "game loop" (!)
    end_of_game = False
    while not end_of_game:

        # ask the player whose turn it is for a guess
        guess = validate_input()

        # clear the screen again, evaluate the player's guess
        os.system("cls")
        #printf '\33c\e[3J'    # if using MacOS X
        print("*   * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *   *")
        print("* * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *\n")

        # special handling for repeated guesses of a letter
        if guess in guessed_letters:
            print(f"FYI: You have already guessed the letter '{guess}'!")

        # case 1: the letter guessed by the player is in the word to guess
        elif guess in chosen_word_to_check:
            if chosen_word_to_check == chosen_word.lower():
                for i in range(word_length):
                    if chosen_word_to_check[i] == guess:
                        display[i] = chosen_word[i]
            # if a special character is involved (cf. the method 'get_word_modified')
            else:
                for i in range(word_length):
                    if chosen_word.lower()[i] == guess:
                        display[i] = chosen_word[i]

                chosen_word_to_check = re.sub(".#", "", chosen_word_to_check)

                for i in range(len(chosen_word_to_check)):
                    if chosen_word_to_check[i] == guess:
                        display[i] = chosen_word[i]

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
                print(f"--- The word to be guessed was '{chosen_word}'!")
                players[word_setter]["score"] += 1

        # display of the word to be guessed
        print(f"{' '.join(display)}")

        # end of the game, scenario 2: the player guessed the word
        if "_" not in display:
            end_of_game = True
            print(winner)
            print("\nCONGRATULATIONS! - You have guessed the word!")
            print(":-D")
            players[word_guesser]["score"] += 1

        # display of the gallows and the list of guessed letters
        print(stages[lives])
        print("\t\tyour inputs: ", end="")
        print(len(guessed_letters), end =" ")
        print(f"(<-- guessed wrong: {nr_of_guesses - lives})")
        print("\t\t", end="")
        print(guessed_letters)
        print()

    # reset / update of variables
    rounds += 1
    lives = nr_of_guesses
    players[word_setter]["matches"] += 1
    players[word_guesser]["matches"] += 1
    all_words_so_far.append(chosen_word)

    # continuation / termination of the game
    print("\n--- CONTINUE, RESTART, OR LEAVE? ---")
    while True:
        player_choice = input("  Enter '1', if you want immediately to continue!\n"
                              "  Enter '2', if you want to get a current game statistic before!\n"
                              "  Enter '3', if you want to restart the game (to change the settings)!\n"
                              "  Enter '4', if you want to quit the game!\n"
                              "  --> Your choice: ")
        if player_choice == "1":
            word_setter, word_guesser = change_players(players, word_setter, word_guesser)
            play_multiplayer_version(players, word_setter, word_guesser, lives, stages, rounds, all_words_so_far)
            break
        elif player_choice == "2":
            show_statistic_multiplayer(players, lives, rounds, all_words_so_far)
            word_setter, word_guesser = change_players(players, word_setter, word_guesser)
            play_multiplayer_version(players, word_setter, word_guesser, lives, stages, rounds, all_words_so_far)
            break
        elif player_choice == "3":
            start()
            break
        elif player_choice == "4":
            print("\n  GOODBYE!")
            break
        else:
            print("Invalid input! -->")


def start():
    """ Display the 'hangman' logo, briefly introduce the game, define basic game settings
    according to the player's/players' preferences, and start the game. """
    # clear the screen, print the game's ASCII logo
    os.system("cls")
    # printf '\33c\e[3J'    # if using MacOS X
    print(logo)
    print()

    introduce_the_game()

    # --> set basic parameters according to the player's choices - and start the game! <--

    # clear the screen again
    os.system("cls")
    # printf '\33c\e[3J'    # if using MacOS X

    # let the player(s) choose between computer version and multiplayer version
    print("\n========================================================================\n")
    print("\t*** GAME SETTINGS ***\n")
    print("(A)")
    print("Do you want the computer to provide words to be guessed or would you like\n" +
          "to compete against other players?")
    score = 0
    rounds = 0
    all_words_so_far = []
    while True:
        player_choice = input("--> Enter 1 for the computer version or 2 for the multiplayer version: ")
        # if the computer version is selected:
        if player_choice == "1":
            # let the player choose a wordlist ()
            wordlist = choose_wordlist()
            print()
            # let the player choose a difficulty level
            lives, stages = choose_level()
            # start the game's computer version
            play_computer_version(wordlist, lives, stages, score, rounds, all_words_so_far)
            break
        # if the multiplayer version is selected:
        elif player_choice == "2":
            # store a players dictionary, based on their inputs, and define who will start
            players, word_setter, word_guesser = get_players()
            print()
            # let the players choose a difficulty level
            lives, stages = choose_level()
            # start the game's multiplayer version
            play_multiplayer_version(players, word_setter, word_guesser, lives, stages, rounds, all_words_so_far)
            break
        else:
            print("Invalid input! -->")


start()
