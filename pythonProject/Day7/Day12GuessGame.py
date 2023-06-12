from random import randint

from GuessGameArt import logo


def random_number():

    chose_number = randint(1, 100)
    return chose_number


def Guessing_Game(number_to_guess):
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I am thiking of a number between 1 and 100.")

        if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
            attempts = 5
        else:
            attempts = 10
        print(number_to_guess)

        game_on = True
        while attempts > 0 and game_on:
            attempts -= 1
            user_guessed = int(input("Make a guess: "))
            if user_guessed == number_to_guess:
                print(f"You got it! The answer was {user_guessed}")
                game_on = False
            elif user_guessed < number_to_guess:
                print(f" Too low.\n Guess again. \n You have {attempts} attempts remaining to guess the number.")
            else:
                print(f" Too high.\n Guess again. \n You have {attempts} attempts remaining to guess the number.")
            if attempts == 0 and game_on:
               print(" You've run out of guesses, you lose.")

while input("Would you like to play a game of guessing? 'Yes' or 'No'").lower() == 'yes':
      Guessing_Game(number_to_guess=random_number())