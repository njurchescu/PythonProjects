from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.\n")

bidders = {}


def add_bidder():
    name_of_bidder = input("What is your name?: ")
    amount_bidded = int(input("Whats' your bid?: $"))
    bidders[name_of_bidder] = amount_bidded


def acution_winner():
    highest_bidder_bid = 0
    winner = ""
    winners = {}
    for bidder in bidders:
        if bidders[bidder] > highest_bidder_bid:
            highest_bidder_bid = bidders[bidder]
    for i in bidders:
        if bidders[i] == highest_bidder_bid:
            winners[i] = highest_bidder_bid
    print(f"Winner/s is/are {winners}")


bidders_left = True

while bidders_left:

    add_bidder()
    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if other_bidders == "yes":
        clear()
    else:
        bidders_left = False
        acution_winner()

print(bidders)
