from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(fun=l_paddle.move_up, key='w')
screen.onkeypress(fun=l_paddle.move_down, key='s') #* Reminder: don't add the () when passing a function as an arguement 
screen.onkeypress(fun=r_paddle.move_up, key='i')
screen.onkeypress(fun=r_paddle.move_down, key='k')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    
    #Detect collision with top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    #Detect R paddle miss
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()
        
    #Detect L paddle miss
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()

#TODO Create the screen
#TODO Create and move a paddle
#TODO Create another paddle
#TODO Create the ball and make it move
#TODO Detect collision with wall and bounce
#TODO Detect collision with paddle
#TODO Detect when paddle misses
#TODO Keep score