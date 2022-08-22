import os
from art import logo

auction = []

def add_bidders(bidder_name, bid_value):
    new_bid = {}
    new_bid["name"] = bidder_name
    new_bid["bid"] = bid_value
    auction.append(new_bid)

def highest_bidder(list_of_bids):
    top_bidder = ''
    top_bid = 0
    for bidder in list_of_bids:
        if bidder["bid"] > top_bid:
            top_bid = bidder["bid"]
            top_bidder = bidder["name"]
    print(f"The highest bidder is {top_bidder}!")

print(logo)
print("Welcome to the Secret Auction program.")

stop_auction = False
while not stop_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: £"))
    add_bidders(name, bid)
    
    stop = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if stop == 'no':
        stop_auction = True
        os.system('cls')
        highest_bidder(auction)
    else:
        os.system('cls')



