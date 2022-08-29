import random
import os
import art
from game_data import data

def choose_person():
    """Choose and a person from the list."""
    return random.choice(data)

def format_data(person):
    """Takes the person data and returns the printable format."""
    name = person['name']
    description = person['description']
    country = person['country']
    return f"{name}, a {description}, from {country}."
    
def correct(guess, a_followers, b_followers):
    """Use if statement to check if user is correct."""
    if a_followers > b_followers: #* if A > B, did you guess A?
        return guess == 'A'
    else: #* if B > A, did you guess B?
        return guess == 'B'
        
def game():
    wrong = False # switch for the while loop
    score = 0 # score counter
    person_a = choose_person()
    while not wrong: # keep looping until user makes a mistake
        os.system('cls') # clear the terminal each loop
        person_b = choose_person()
        while person_a == person_b: # choose another person if they're the same 
            person_b = choose_person()
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}.")
        
        # Print information from the dictionary for each person
        print(f"Compare A: {format_data(person_a)}")
        print(art.vs)
        print(f"Against B: {format_data(person_b)}")
        
        # Obtain answer from user and check the answer
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if correct(answer, person_a['follower_count'], person_b['follower_count']):
            score += 1 # add to score
            person_a = person_b # person_a is now the previous person_b
        else:
            wrong = True # switch to end the game
            os.system('cls') # clear the screen
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}") # print final score
game()