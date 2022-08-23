from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.write_score()
    
    def write_score(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.level += 1
        self.clear()
        self.write_score()
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
