import random
from replit import clear
import os


end_of_game = False

from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
print(f'\nPssst, the solution is {chosen_word}.\n')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

        guess = input("Guess a letter: \n").lower()

        clear()

        print(f"You entered: {guess}")

        if guess in display:
            print(f"You already guessed {guess}.")

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #TODO-2: - If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1.
        if guess not in chosen_word or guess == '':

             lives -= 1
             # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
             print(stages[lives])

             if lives > 0:

                 print("You guessed wrong!\n Try again.\n")
                 print(f"Number of lives left is {lives}")

             elif lives == 0:
                # If lives goes down to 0 then the game should stop and it should print "You lose."
                end_of_game = True
                print(f"Number of lives is {lives}.\n You lose!")


#Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

#Check if user has got all letters.
        if "_" not in display:
           end_of_game = True
           print("You win.")
