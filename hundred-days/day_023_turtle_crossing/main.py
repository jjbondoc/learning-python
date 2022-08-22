import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager() #create cars
scoreboard = Scoreboard()

screen.onkeypress(fun=player.up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    #Move cars across the screen
    car_manager.move_cars()
    #Detect player reaching end zone
    if player.ycor() > 280:
        player.reset()
        car_manager.increase_speed()
        scoreboard.update_score()
    #Detect player-car collision
    for car in car_manager.cars:
        if car.distance(player) < 30 and player.ycor() < car.ycor() + 20 and player.ycor() > car.ycor() - 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
