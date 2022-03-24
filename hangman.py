#A simple python hangman game based on Genshin Impact

from operator import le
import random
from typing import no_type_check


print("Welcome to GENSHIN IMPACT Hangman Game!")

collection_of_words = ["JEAN","HUTAO","ZHONGLI","GANYU","KAZUHA","EULA","RAIDENEI","YAEMIKO"] #set a list of words
word_to_guess = random.choice(collection_of_words) #select a random word from the list

no_of_attempts = 8 #no of turns the player gets to guess the letters

letters_guessed = "" #holds the correctly guessed letters

while no_of_attempts > 0:
    user_guess = input("\nEnter a letter: ").upper()

    if user_guess in word_to_guess:

        print(f"You guessed a correct letter!")

    else:
        no_of_attempts -= 1
        print(f"OOPS.. Your guess {user_guess} is incorrect.. {no_of_attempts} attempts left..")
    
    letters_guessed = letters_guessed + user_guess

    count_wrong_letters = 0

    for letter in word_to_guess:
        if letter in letters_guessed:
            print(f"{letter}",end="")
        
        else:
            print("_",end="")
            count_wrong_letters += 1

    if count_wrong_letters == 0:
        print(f"\nContrats! Your word was {word_to_guess}")
        break


    