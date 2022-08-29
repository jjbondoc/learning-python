from turtle import Turtle
import random

START_SPEED = 10

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle') #* Because we are inheritting 
        self.color('white')
        self.penup()
        self.x_speed = START_SPEED
        self.y_speed = START_SPEED
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
    
    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        
    def bounce_y(self):
        self.y_speed *= -1
    
    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.9