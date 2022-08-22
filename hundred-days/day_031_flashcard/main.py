from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
next_word = {}

def next_card():
    """Choose a new card from the list."""  
    global next_word, flip_timer
    
    window.after_cancel(flip_timer)
      
    next_word = random.choice(word_list)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=next_word['French'], fill='black')
    
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    """Remove the card from the deck,
    then choose the next card."""
    word_list.remove(next_word)
    df_to_learn = pandas.DataFrame(word_list)
    df_to_learn.to_csv('./data/words_to_learn.csv', index=False)
    next_card()
    
def flip_card():
    """Flip to the other side of the card."""
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=next_word['English'], fill='white')

#------------------------- DATA ---------------------------#
try:
    df = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('./data/french_words.csv')
finally:
    word_list = df.to_dict(orient='records')

#-------------------------- UI ----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)
card = canvas.create_image(400, 263, image=card_front)
#Text
title = canvas.create_text(400, 150, text="Title", font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text="Word", font=('Arial', 60, 'bold'))

#Butons
right_button = Button(image=right_img, highlightthickness=0, relief='flat', borderwidth=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, relief='flat', borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()