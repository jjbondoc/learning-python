import os
from art import logo

auction = {}    

def highest_bidder(bids):
    top_bid = 0
    winner = ''
    for name in bids:
        if bids[name] > top_bid:
            top_bid = bids[name]
            winner = name

    print(f"The highest bidder is {winner}!")

print(logo)
print("Welcome to the Secret Auction program.")

stop_auction = False
while not stop_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: £"))
    auction[name] = bid
    
    stop = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if stop == 'no':
        stop_auction = True
        os.system('cls')
        highest_bidder(auction)
    else:
        os.system('cls')



