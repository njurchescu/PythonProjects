import random
from higherlowerart import logo, vs
from higher_lower_game_data import data



def get_celeb():
    return random.choice(data)

def compare_celebrietes(A, B, score):
    '''Function to compare A and B based on user's choice'''
    user = input("Who has more followers?  'A' or 'B':").upper()

    if (A > B and user == 'A') or (A < B and user == 'B'):
       return score + 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return score - score

def play_game():
    '''Function to start the game'''
    print(logo)
    score = 0

    celeb_1 = get_celeb()
    game_on = True
    while game_on:

          celeb_2 = get_celeb()

          choice_A = celeb_1['follower_count']
          choice_B = celeb_2['follower_count']

          print(  f"Compare A: {celeb_1['name']} , a {celeb_1['description']}, from {celeb_1['country']}.")
          print(vs)
          print(f"Compare B: {celeb_2['name']} , a {celeb_2['description']}, from {celeb_2['country']}.")

          score = compare_celebrietes(A=choice_A, B=choice_B, score=score)
          celeb_1 = celeb_2
          if score > 0:
              print(f"You are right! Current score: {score}")
          else:
              game_on = False

play_game()

