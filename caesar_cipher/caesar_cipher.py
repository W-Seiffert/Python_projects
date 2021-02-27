"""
Feb. 2021
@author: Walter Seiffert

Beginner's program that allows to encode or decode messages based on an implementation of
the Caesar cipher. - Note: The basic structure of the program was inspired by a lesson of
Dr. Angela Yu's 'Python Bootcamp', as offered on the learning platform Udemy (s. '100 Days 
of Code - The Complete Python Pro Bootcamp for 2021' --> Day 8); the 'chunkstring' function's 
code is borrowed from Antti Haapala, s. his accepted answer (Feb 13, 2016) to 
https://stackoverflow.com/questions/35381065/dynamic-border-around-text-in-python.
"""


import caesar_cipher_art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
			'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
			'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    """ encode/decode a string with Caesar's substitution cipher, taking as parameters the text, 
    the shift value and the direction passed to the function; return the result """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    return end_text


def chunkstring(string, length):
    """ slice a string into chunks of letters of a certain length, defined by the length argument 
    passed to the function (--> note the third value in the 'range' function, that specifies the
    incrementation or the step taken after each iteration); return the result """
    return (string[0+i:length+i] for i in range(0, len(string), length))


# --- RUNNING THE PROGRAM ---

os.system("cls")
# printf '\33c\e[3J'     # if using Mac OS X
print(caesar_cipher_art.logo)

print(" | Welcome to this modest little program that offers just a very simple\n"
      " | implementation of the famous 'Caesar cipher'.\n"
      " | \n"
      " | The 'Caesar cipher', ascribed in a basic form to Julius Caesar (and,\n"
      " | in a slight variation, to his successor Augustus) by the Roman historio-\n"
      " | grapher Suetonius, may be classified in terms of modern cryptography as\n"
      " | 'monoalphabetic substitution cipher'.\n")
proceed = input("--> Press ENTER to get a very short orientation! ")

os.system("cls")
# printf '\33c\e[3J'     # if using Mac OS X
print()
print(" | As the name suggests, a 'substitution cipher' works essentially by substituting\n"
      " | (usually all) characters or groups of characters of a 'plaintext' (the one that is\n"
      " | to be encrypted) with different characters or groups of characters in a resulting\n"
      " | 'ciphertext', according to fixed rules of substitution. It must be emphasized,\n" 
      " | however, that regarding this encryption technique there are actually lots of\n"
      " | variations whose particularities cannot be tackled here.\n"
      " |\n"
      " |    Of interest are in the present context only 'monoalphabetic' ciphers, ore more\n"
      " | precisely: 'monoalphabetic ciphers over natural languages' (the curious reader may\n"
      " | be referred to an amusing introduction to the topic, written for a wider audience\n"
      " | by the mathematician Albrecht Beutelspacher: Cryptology. An Introduction to the Art\n"
      " | and Science of Enciphering, Encrypting, Concealing, Hiding and Safeguarding [...],\n"
      " | Washington DC 1994). Now, a cipher may be defined as 'monoalphabetic' if any letter\n"
      " | of the alphabet used in the plaintext is always enciphered by the same letter in the\n"
      " | ciphertext. In other words, you make use of a 'ciphertext alphabet' whose elements\n"
      " | are uniquely linked to elements of the alphabet used in the plaintext.\n"
      " |\n"
      " |    The 'Caesar cipher' is a rather simple version of this type in several respects:\n"
      " | (a) it is a 'simple substitution cipher', that is: it operates on single letters;\n"
      " | (b) 'plaintext' and 'ciphertext' are defined over the same alphabet (of 26 letters);\n"
      " | (c) there is only one rule regulating the letter substitution (--> 'shift the letter\n"
      " |     by 'n' positions to the right/to the left'! - to be defined via a shift value)\n")

proceed = input("--> Press ENTER for a final overview sketch! ")
os.system("cls")
# printf '\33c\e[3J'     # if using Mac OS X
print()
print(" | Operating scheme of the cipher version implemented here:\n"
      " | (grossly simplified)\n"
      " |\n"
      " | A l p h a b e t:\n"
      " | ----------------\n"
      " |   a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z\n"
      " |\n"
      " |\n"
      " | E N C O D I N G:\n"
      " | ----------------\n"
      " |   PLAINTEXT, as entered by the user\n"
      " |   + shift value 'n': defined by the user\n"
      " |      -->  encryption: shift any letter by 'n' positions,\n" 
      " |           going 'forward' in the alphabet\n"
      " |           (* the direction may be reversed using a negative shift value!)\n"
      " |      -->  CIPHERTEXT\n"
      " |\n"
      " |\n"
      " | D E C O D I N G:\n"
      " | ----------------\n"
      " |   CIPHERTEXT, as entered by the user\n"
      " |   + shift value 'n': defined by the user\n"
      " |      -->  decryption: shift any letter by 'n' positions,\n"
      " |           going 'backward' in the alphabet\n"
      " |           (* the direction may be reversed using a negative shift value!)\n"
      " |      -->  PLAINTEXT\n")

proceed = input("--> Press ENTER to get started!")
os.system("cls")
# printf '\33c\e[3J'     # if using Mac OS X


# --- STARTING THE PROGRAM'S MAIN LOOP ---

run_cc = True
while run_cc:

    # user input: cipher direction (encode/decode)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Type 'encode' to encrypt or 'decode' to decrypt a message:")
    while True:
        direction = input("-- ")
        if direction.lower() == "encode" or direction.lower() == "decode":
            break
        else:
            print("Invalid input! --> 'encode' or 'decode', please!")

    # user input: text to encode/decode
    text = input("\nAll right, now enter your message please:\n-- ").lower()

    # user input: shift number
    print("\nFinally, please enter the desired shift value:")
    while True:
        try:
            shift = int(input("-- "))
            shift = shift % 26
            break
        except ValueError:
            print("Invalid input! --> Enter a whole number, please!")

    # encryption, using the 'caesar' function
    message = caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # output of the result, using the 'chunkstring' function
    print("\nOkay, that's it - all of your inputs have been processed.")
    print(f"Now, here is your {direction}d text:\n")
    width = 50
    print('  +--' + '-' * width + '--+')
    for line in chunkstring(message, width):
        print('  |  {0:^{1}}  |'.format(line, width))
    print('  +--' + '-'*(width) + '--+')

    print()
    print("=======================================")

    # continue or quit
    while True:
        proceed = input("Would you like to try it again? (Y / N)\n")
        if proceed.lower() == "n":
            print("\n  G O O D B Y E !\n")
            run_cc = False
            break
        elif proceed.lower() == "y":
            print("\nGreat! Then just go ahead ...")
            print()
            break
        else:
            print("Invalid input! -->")
