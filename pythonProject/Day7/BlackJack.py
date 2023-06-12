import random
from BlackJackArt import logo


game_on = True



def blackjack():
    '''Start the game of Blackjack'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # clear()
    print(logo)
        # We create a dictionary to hold our player's cards
    players = {
            "user_cards": [],
            "computer_cards": [],
    }
 # We give each player two random cards from the deck
    players["user_cards"].append(random.choice(cards))
    players["user_cards"].append(random.choice(cards))

    players["computer_cards"].append(random.choice(cards))
    players["computer_cards"].append(random.choice(cards))
# We calculate the sum of the cards for each player
    my_score = sum(players['user_cards'])
    computer_score = sum(players['computer_cards'])

    # We display the cards and score/sum for player user
    print(f"Your cards: {players['user_cards']}, current score {my_score}")
    # We only display first cards for player computer
    print(f"Computer's first card: {players['computer_cards'][0]}")
    # We create a booleab variable to make our game run for as long as its value is true
    game_on = True

    # Function to give cards to the user
    def user_hand():
        '''Function to return the user's hand'''

        # We calculate the user's sum of cards
        user_hand = sum(players['user_cards'])
        # If the sum is less then 21 then ask user if he wants another card and we add it to its hand('user_cards' key from players dictionary)
        if user_hand < 21:
            while user_hand < 21:
                user_choice = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
                if user_choice == 'y':
                    players["user_cards"].append(random.choice(cards))
                    a_case = players["user_cards"][-1]
                    user_hand = sum(players['user_cards'])

                    # If the new random card is 11 and the sum of the hand is over 21 then the random card becomes 1
                    if a_case == 11 and user_hand > 21:
                        players["user_cards"][-1] = 1
                        user_hand = sum(players['user_cards'])
                        # print(f"User cards are: {players['user_cards']}")
                    print(f"Your cards: {players['user_cards']}, current score {user_hand}")
                else:
                    return user_hand
            if user_hand >= 21:
                # print(f"User cards are: {players['user_cards']}")
                return user_hand
        else:
            return user_hand

    # Function to give cards to the computer
    def computer_hand():
        '''Function to return the computer's hand'''
        computer_hand = sum(players['computer_cards'])
        # If the sum is less then 17 then computer gets a new random card until the sum is 17 or over 17
        if computer_hand < 17:
            while computer_hand < 17:
                players["computer_cards"].append(random.choice(cards))
                computer_hand = sum(players['computer_cards'])
                # print(f"Computer cards are: {players['computer_cards']}")
                if computer_hand >= 17:
                    return computer_hand
        else:
            return computer_hand

    user_blackjack = sum(players['user_cards'])
    computer_blackjack = sum(players['computer_cards'])
# We check if the first two random cards assigned to user or computer are 10 and 11
            # and if yes, then its Blackjack and the game ends
            # We then ask the user if he wants to play a new game of blackjack
    if user_blackjack == 21 and computer_blackjack == 21:
       print(f"Your final hand: {players['user_cards']}, final score: {my_score}")
       print(f"Computer final hand: {players['computer_cards']}, final score: {computer_score}")
       print("You both win with a Blackjack!")
       game_on = False
                # blackjack()
    elif user_blackjack == 21:
         print(f"Your final hand: {players['user_cards']}, final score: {my_score}")
         print(f"Computer final hand: {players['computer_cards']}, final score: {computer_score}")
         print("You win with a Blackjack!")
         game_on = False
                # blackjack()
    elif computer_blackjack == 21:
         print(f"Your final hand: {players['user_cards']}, final score: {my_score}")
         print(f"Computer final hand: {players['computer_cards']}, final score: {computer_score}")
         print("You lose, computer wins with a Blackjack!")
         game_on = False
                # blackjack()
    else:
                # We creat two new variables to get the return from user_hand and computer_hand functions
         user_player = user_hand()
         computer_player = computer_hand()
            #We loop through the player's hands to see who won and then we set the game_on variable to False to make sure
            # to exit the loop and aviod a bug
            # Then we call the function itself until the user types n when asked if he wants to play a game of Blackjack
    while game_on:
          if user_player <= 21 and computer_player <= 21:
             if user_player == computer_player:
                print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                print("Its a DRAW!")
                game_on = False
                        # blackjack()
             elif user_player >  computer_player:
                  print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                  print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                  print("You win!")
                  game_on = False
                        # blackjack()
             else:
                  print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                  print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                  print("You lose!")
                  game_on = False
                        # blackjack()
          elif user_player > 21 and computer_player > 21:
               if user_player == computer_player:
                  print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                  print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                  print("You both lose but its still a DRAW!")
                  game_on = False
                        # blackjack()
               elif user_player > computer_player:
                    print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                    print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                    print("You both lose but you lose lose!")
                    game_on = False
                        # blackjack()
               else:
                   print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                   print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                   print("You both lose but you still win!")
                   game_on = False
                        # blackjack()
          elif user_player > 21 and computer_player <= 21:
                print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
                print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
                print("You lose!")
                game_on = False
                    # blackjack()
          else:
               print(f"Your final hand: {players['user_cards']}, final score: {user_player}")
               print(f"Computer final hand: {players['computer_cards']}, final score: {computer_player}")
               print("You Win!")
               game_on = False
                    # blackjack()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  blackjack()

