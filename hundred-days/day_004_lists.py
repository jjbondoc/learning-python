from ast import Or
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hands = [rock, paper, scissors]
user_input = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# try to do something, it there's an error, run the except block
try:
    if int(user_input) not in [0, 1, 2]:
        print("Invalid choice, try again.")
        exit(0)
except ValueError:
    print("That's not a number.")
    exit(0)

user_hand = hands[int(user_input)]
computer_hand = random.choice([rock, paper, scissors])

print(f"{user_hand}")
print(f"Computer chose:\n{computer_hand}")

if user_hand == computer_hand:
    print("It's a draw!")
elif ((user_hand == rock and computer_hand == paper) or
      (user_hand == paper and computer_hand == scissors) or
      (user_hand == scissors and computer_hand == rock)):
    print("You lose!")
else:
    print("You win!")