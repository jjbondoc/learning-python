print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

cross_road = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if cross_road == "left":
    lake = input('You\'ve come to a lake. There is an island in the iddle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "blue":
            print("You get eaten by beasts.\nGame Over.")
        elif door == "red":
            print("You are burned by fire.\nGame Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("You are attacked by trout.\nGame Over.")
else:
    print("You fall into a hole.\nGame Over.")