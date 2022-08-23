import pandas as pd
import turtle

raw_df = pd.read_csv('50_states.csv')
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()

def draw(state_name):
    row = raw_df[raw_df['state'] == state_name]
    print(int(row['x']))
    timmy.goto(int(row['x']), int(row['y']))
    timmy.write(state_name, align='center', font=("Arial", 10, 'normal'))

image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.screensize(canvwidth=730, canvheight=500)
screen.title('U.S. State Game')
screen.addshape(image)

turtle.shape(image)

state_list = raw_df['state'].to_list()
correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f'{len(correct_guesses)}/50 States', prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        break
    if answer_state not in correct_guesses and answer_state in state_list:
        correct_guesses.append(answer_state)
        draw(answer_state)

missing_states = {
    "state":list(set(state_list) - set(correct_guesses))
}

pd.DataFrame(missing_states).to_csv('states_to_learn.csv')