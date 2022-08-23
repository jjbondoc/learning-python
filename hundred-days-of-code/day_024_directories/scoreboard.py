from tkinter import CENTER
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier New', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.current_score = 0
        with open('high_score.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.clear()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('high_score.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.current_score = 0
        self.update_score()
    
    def increase_score(self):
        self.current_score += 1
        self.update_score()
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        