from turtle import Turtle, pos

class Paddle(Turtle):
    
    def __init__(self, position) -> None:
        super().__init__()
        self.shape('square') #* Because we are inheritting, we can reference those functions and attributes 
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    
    def move_up(self):
        ycor = self.ycor()
        self.sety(ycor + 20)
    
    def move_down(self):
        ycor = self.ycor()
        self.sety(ycor - 20)