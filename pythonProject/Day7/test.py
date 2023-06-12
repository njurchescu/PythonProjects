import random

from GuessGameArt import logo


def random_number():
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    chose_number = random.choice(numbers)
    return chose_number



def user_guess():
    guess = int(input("Make a guess: "))
    return guess

def check_guess(random_num,user_guess,game):
        if user_guessed == number_to_guess:
           game = False
        elif user_guess < random_num:
            print(f" Too low.\n Guess again. \n You have {attempts} attempts remaining to guess the number.")
        else:
            # user_guess > random_num:
             print (f" Too high.\n Guess again. \n You have {attempts} attempts remaining to guess the number.")



while input("Would you like to play a game of guessing? 'Yes' or 'No'").lower() == 'yes':
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thiking of a number between 1 and 100.")
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
        attempts = 5
    else:
        attempts = 10

    number_to_guess = random_number()
    print(number_to_guess)
    game_on = True
    while attempts > 0 and game_on:
        user_guessed = user_guess()
        attempts -= 1
        game_on = check_guess(random_num=number_to_guess, user_guess=user_guessed,game=game_on)
        if game_on == False:
            print(f"You got it! The answer was {user_guessed}")
        if attempts == 0 and game_on:
            print(" You've run out of guesses, you lose.")