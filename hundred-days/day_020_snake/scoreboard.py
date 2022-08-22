from tkinter import CENTER
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier New', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.current_score = 0
        self.clear()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write_score()
        
    def write_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        